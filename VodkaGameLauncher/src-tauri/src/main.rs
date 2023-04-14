/*
    disable command prompt on windows machines
*/
#![cfg_attr(
    all(not(debug_assertions), target_os = "windows"),
    windows_subsystem = "windows"
)]



/*

imports

*/
use std::fs;
use std::path::Path;
use std::fmt::Write;
use std::process::Command;

use std::collections::HashMap;

use serde::{Deserialize, Serialize};
use serde_json::{Map, Value};
use serde_json::json;

use md5;
use tokio::fs as tokio_fs;
use tokio::task;
use tokio::io::{AsyncWriteExt};
use tokio::runtime::Runtime;
use reqwest::Client;
use reqwest::Url;
use futures::stream::StreamExt;
use tauri::api::dialog::FileDialogBuilder;
use dirs;
use tauri::Manager;
use window_shadows::set_shadow;

/*

    structs


*/

#[derive(Serialize, Deserialize)]
struct JsonFileContents {
    json: String,
}

#[derive(Serialize, Deserialize)]
struct FileContents {
    version: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct DirectoryStructure {
    #[serde(rename = "type")]
    node_type: String,
    path: String,
    hash: String,
    children: Option<Vec<DirectoryStructure>>,
}

#[derive(Debug, Deserialize, Serialize)]
struct ComparisonResult {
    missing: Map<String, Value>,
    mismatched: Map<String, Value>,
    total: usize,
}

#[derive(Serialize, Deserialize)]
struct GameSettingsCreation {
    game: String,
    game_dir: String,
    version: String,
}

/*

    helper functions writing to files, writing json to file etc.. 


*/

fn write_file(path: &str, content: &str) -> Result<(), std::io::Error> {
    std::fs::write(path, content)
}

fn read_json_file(filename: &str) -> Result<FileContents, Box<dyn std::error::Error>> {
    let file = fs::File::open(filename)?;
    let reader = std::io::BufReader::new(file);
    let contents: FileContents = serde_json::from_reader(reader)?;
    Ok(contents)
}

fn write_json_file(filename: &str, contents: &impl Serialize) -> Result<(), Box<dyn std::error::Error>> {
    let file = fs::File::create(filename)?;
    let writer = std::io::BufWriter::new(file);
    serde_json::to_writer(writer, contents)?;
    Ok(())
}



/*

    general functions...

*/

fn compare_json_objects(json1: &Value, json2: &Value) -> ComparisonResult {
    let mut missing = Map::new();
    let mut mismatched = Map::new();

    if let Value::Object(map1) = json1 {
        if let Value::Object(map2) = json2 {
            // Compare keys in map1 against map2
            for (key, value) in map1.iter() {
                if !map2.contains_key(key) {
                    missing.insert(key.to_owned(), Value::String("file does not exist".to_owned()));
                } else if map2[key] != *value {
                    mismatched.insert(key.to_owned(), Value::String("failed hash match".to_owned()));
                }
            }

            // Compare keys in map2 against map1
            for (key, value) in map2.iter() {
                if !map1.contains_key(key) {
                    missing.insert(key.to_owned(), Value::String("file does not exist".to_owned()));
                }
            }
        }
    }
    
    let total = missing.len() + mismatched.len();

    ComparisonResult {
        missing,
        mismatched,
        total,
    }
}


fn generate_directory_structure(directory_path: &Path, parent_path: &str) -> HashMap<String, String> {
    let mut result = HashMap::new();

    for item in directory_path.read_dir().expect("Failed to read directory") {
        if let Ok(item) = item {
            let item_path = item.path();
            let item_name = item.file_name().to_string_lossy().to_string();

            if item_path.is_file() {
                if item_name == "directory_map.json" || item_name == "game_version.json" || item_name == "game_install_config.json" {
                    continue; // Skip these files
                }

                let hash = format!("{:x}", md5::compute(fs::read(&item_path).unwrap()));

                let mut file_path = String::new();
                if let Some(parent) = parent_path.strip_prefix('/') {
                    write!(file_path, "{}/{}", parent, item_name).expect("Failed to write file path");
                } else {
                    write!(file_path, "{}", item_name).expect("Failed to write file path");
                }

                result.insert(file_path, hash);
            } else if item_path.is_dir() {
                let subdirectory = generate_directory_structure(&item_path, &item_name);

                for (file_path, hash) in subdirectory {
                    let mut full_file_path = String::new();
                    if let Some(parent) = parent_path.strip_prefix('/') {
                        write!(full_file_path, "{}/{}", parent, item_name).expect("Failed to write file path");
                    } else {
                        write!(full_file_path, "{}", item_name).expect("Failed to write file path");
                    }
                    write!(full_file_path, "/{}", file_path).expect("Failed to write file path");

                    result.insert(full_file_path, hash);
                }
            }
        }
    }

    result
}

/*

    commands 


*/

#[tauri::command]
async fn download_me(url: &str, install_path: &str) -> Result<(), Value> {
    const BUFFER_SIZE: usize = 1 * 1024 * 1024; // 1 MB buffer

    let test = url;
    let url = Url::parse(test).map_err(|err| json!({"error": err.to_string()}))?;
    let response = reqwest::get(url).await.map_err(|err| json!({"error": err.to_string()}))?;
    
    let path = Path::new(install_path);
    let parent = path.parent().ok_or_else(|| json!({"error": "Invalid path"}))?;
    
    // Create parent directories if they do not exist
    fs::create_dir_all(parent).map_err(|err| json!({"error": format!("Failed to create directories: {}", err)}))?;
    
    let mut file = tokio::fs::File::create(path).await.map_err(|err| json!({"error": err.to_string()}))?;
    let mut content = response.bytes_stream();
    let mut buffer = vec![0u8; BUFFER_SIZE];

    while let Some(chunk) = content.next().await {
        let chunk = chunk.map_err(|err| json!({"error": err.to_string()}))?;
        file.write_all(&chunk).await.map_err(|err| json!({"error": err.to_string()}))?;

        // Write to buffer instead of concatenating to a string
        buffer.extend_from_slice(&chunk);
        //println!("Received chunk: {:?}", chunk);
    }

    if String::from_utf8_lossy(&buffer).contains("File Must be removed") {
        println!("File must be removed {}", install_path.to_string());
        tokio::fs::remove_file(path).await.map_err(|err| json!({"error": format!("Failed to remove file: {}", err)}))?;
        //return Err(json!({"error": "File must be removed"}));
    }

    Ok(())
}


#[tauri::command]
fn validate_me(params: HashMap<String, String>) -> String {
    let root_path = params.get("root_path").unwrap();
    let json_string = params.get("json_string").unwrap();
    let directory_structure = generate_directory_structure(Path::new(root_path), "");
    let directory_structure_json = serde_json::to_string(&directory_structure).unwrap();
    let directory_structure_value: Value = serde_json::from_str(&directory_structure_json).unwrap();
    let json_value: Value = serde_json::from_str(&json_string).unwrap();
    let diff = compare_json_objects(&directory_structure_value, &json_value);
    let diff_json = serde_json::to_string(&diff).unwrap();
    diff_json
}



#[tauri::command]
fn is_game_installed() -> bool {
    let appdata_path = dirs::data_dir().unwrap();
    let vodkagamelauncher_path = appdata_path.join("vodkagamelauncher");
    let install_game_path = vodkagamelauncher_path.join("game_install_config.json");
    println!("Install game path: {:?}", install_game_path);
    println!("Install game path: {:?}", install_game_path.exists());

    install_game_path.exists()
}


#[tauri::command]
fn create_game_install(params: HashMap<String, String>) -> Result<(), Value> {
    let install_game_path = params.get("game_install_path").unwrap();
    let game_dir = params.get("dir_path").unwrap();
    let live_version = params.get("version").unwrap();
    let appdata_path = dirs::data_dir().unwrap();
    let vodkagamelauncher_path = appdata_path.join("vodkagamelauncher");
    let install_game_path_formated = vodkagamelauncher_path.join("game_install_config.json");
    let path = Path::new(&install_game_path_formated);
    
    let parent = path.parent().ok_or_else(|| json!({"error": "Invalid path"}))?;
    fs::create_dir_all(parent).map_err(|err| {
        json!({"error": format!("Failed to create directories: {}", err)})
    })?;

    let file_contents = GameSettingsCreation {
        game: install_game_path.to_string(),
        game_dir: game_dir.to_string(), 
        version: live_version.to_string(),
    };

    write_json_file(&install_game_path_formated.to_string_lossy(), &file_contents);

    Ok(())
}



#[tauri::command]
fn get_game_install() -> Result<Value, Value> {
    let appdata_path = dirs::data_dir().unwrap();
    let vodkagamelauncher_path = appdata_path.join("vodkagamelauncher");
    let install_game_path_formatted = vodkagamelauncher_path.join("game_install_config.json");
    
    // Read the content of the file into a string
    let file_content = std::fs::read_to_string(&install_game_path_formatted)
        .map_err(|err| json!({"error": format!("Failed to read file: {}", err)}))?;
    
    // Parse the JSON content into a Value
    let json_value: Value = serde_json::from_str(&file_content)
        .map_err(|err| json!({"error": format!("Failed to parse JSON: {}", err)}))?;
    
    Ok(json_value)
}


/*

prompt used to show the directory selection for the user to pick the install location
reason we dont use js for this is because its locked behind security policies where as with using rust
we are not tied to the same security policies :D 

*/

#[tauri::command]
async fn select_directory() -> Option<String> {
    let (tx, mut rx) = tokio::sync::oneshot::channel();

    let _ = task::spawn_blocking(move || {
        FileDialogBuilder::new()
            .pick_folder(|folder_path| {
                let path = folder_path.map(|p| p.to_string_lossy().into_owned());
                let _ = tx.send(path);
            })
            
    })
    .await;

    // did not work as i expected so i loop until we get feedback
    loop {
        match rx.try_recv() {
            Ok(selected_directory) => {
                let select_directory = selected_directory.unwrap_or_default().to_string();
                println!("Selected directory: {:?}", select_directory);
                return Some(select_directory);
            },
            Err(_) => {},
        }
    }
}



/*
   used to start the program
   i originally wrote this to spawn with admin priv, but this could be a security issue if someone was to find offsets and inject into this function...
   so in the rare case that you need to spawn the exe as an admin reach out to me on discord and i can give you the code required to run as elevated
   weirdly during testing there was no UAC prompt which i would expect from spawning process as admin.. :|  again this is another reason i removed
   from public build big potential security issues :( 
    anyway my discord is: v0dka#2805
    
*/
#[tauri::command]
fn start_game(path: &str) {
    let output = Command::new(path)
    .spawn()
    .expect("Failed to launch Notepad");
}

#[tauri::command]
async fn close_splashscreen(window: tauri::Window) {
  // Close splashscreen
  if let Some(splashscreen) = window.get_window("splashscreen") {
    splashscreen.close().unwrap();
  }
  // Show main window
  window.get_window("main").unwrap().show().unwrap();
}

fn main() {
    tauri::Builder::default()
    .setup(|app| {
        let window = app.get_window("main").unwrap();
        #[cfg(any(windows, target_os = "macos"))]
        set_shadow(&window, true).unwrap();
        Ok(())
    })
        .invoke_handler(tauri::generate_handler![is_game_installed,create_game_install,validate_me,select_directory,download_me,get_game_install,start_game,close_splashscreen])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}