<template>
 <Toast />
  <div class="grid">
    
   

    <div class="col-12 text-center">
      Home | News | Support | Discord
     
    </div>
    <div class="col-8 text-center">

      
          <div class="card flex justify-content-center galleria text-center main_image">
              <Galleria ref="galleria" v-model:activeIndex="activeIndex" :value="images" :numVisible="5" containerStyle="width: 1500px" :containerClass="galleriaClass"
                  :showThumbnails="showThumbnails" :showItemNavigators="true" :showItemNavigatorsOnHover="true" :circular="true" :autoPlay="true" :transitionInterval="8000">
                  <template #item="slotProps">
                      <img :src="slotProps.item.itemImageSrc" :alt="slotProps.item.alt" :style="[{ width: !fullScreen ? '100%' : '', display: !fullScreen ? 'block' : '' }]" />
                  </template>
                  <template #thumbnail="slotProps">
                      <div class="grid grid-nogutter justify-content-center">
                          <img :src="slotProps.item.thumbnailImageSrc" :alt="slotProps.item.alt" style="display: block" />
                      </div>
                  </template>
                  <template #footer>
                      <div class="custom-galleria-footer">
                          
                          <span v-if="images" class="title-container">
                              <span class="title">{{ images[activeIndex].title }}</span>
                              <span>{{ images[activeIndex].alt.substr(0, 100) + " ... read more" }}</span>
                          </span>
                          
                      </div>
                  </template>
              </Galleria>
          </div>
          
          
          <div class="col-12">
            <div class="play_button" v-if="play_button == 'play'">
              <Button label="Play" icon="pi pi-play" severity="success" size="large" @click="PlayGame" />
            </div>
            <div class="play_button" v-if="play_button == 'update'">
              <Button label="Updating" severity="warning" icon="pi pi-spinner" iconPos="left">
                <span class="pi pi-spinner pi-spin"></span>  &nbsp Updating
                
              </Button>
            </div>
          </div>
        
          
        
    </div>
    <div class="col-4 text-center">
      <div class="side_image">
        <Image src="http://localhost/test_images/main.png" alt="Image" width="580"  />
        Annoucements | Community Posts | Patch Notes
        <div class="py-2">
          Annoucement
        </div>
        <div class="py-6">
          blah blah im content blah blah blah woo i have more content blah blah blah blah blah
        </div>
      </div>
    </div>
      
    <div class="col-12 text-center" v-if="current_file">
      <div class="py-5" v-if="total_files > 0">
        total files left {{ total_files }}    Current Download: {{ current_file }}
        <ProgressBar mode="indeterminate" style="height: 6px; width:1650px; transform: translate(-10px);" ></ProgressBar>
      </div>
      <div class="py-5" v-if="total_files == 0 || total_files == ''">
        {{ current_file }} 
        <ProgressBar mode="indeterminate" style="height: 6px; width:1650px; transform: translate(-10px);" ></ProgressBar>
      </div>
    </div>
  </div>
  
  
  
</template>


<script setup>
  import { useToast } from "primevue/usetoast";
  import { ref, onMounted, computed, defineExpose } from "vue";
  import { invoke } from "@tauri-apps/api/tauri";
  import { getClient, Body, ResponseType } from '@tauri-apps/api/http';
  const toast = useToast();
  const news_feed = ref();
  const show_more = ref(false);
  const total_news = ref();
  const default_data = ref();
  const total_files = ref(0);
  const current_file = ref();
  const play_button = ref("update");
  const domain = "http://127.0.0.1:8090/";

  const galleria = ref();
  const images = ref();
  const activeIndex = ref(0);
  const showThumbnails = ref(false);
  const fullScreen = ref(false);


  const PhotoService = {
        getData() {
            return [
                {
                    itemImageSrc: 'http://localhost/test_images/first.png',
                    thumbnailImageSrc: 'http://localhost/test_images/first.png',
                    alt: 'this is the content of the news article we are updating servers to do xyz and we are doing much more maintanance tasks to achieve better performance across the service infrastrucutre ',
                    title: 'Title 1'
                },
                {
                    itemImageSrc: 'http://localhost/test_images/second.png',
                    thumbnailImageSrc: 'http://localhost/test_images/second.png',
                    alt: 'content 2',
                    title: 'Title 2'
                },
                {
                    itemImageSrc: 'http://localhost/test_images/third.png',
                    thumbnailImageSrc: 'http://localhost/test_images/third.png',
                    alt: 'content 3',
                    title: 'Title 3'
                },
                {
                    itemImageSrc: 'http://localhost/test_images/fourth.png',
                    thumbnailImageSrc: 'http://localhost/test_images/fourth.png',
                    alt: 'content 4',
                    title: 'Title 4'
                },
                {
                    itemImageSrc: 'http://localhost/test_images/fifth.png',
                    thumbnailImageSrc: 'http://localhost/test_images/fifth.png',
                    alt: 'content 5',
                    title: 'Title 5'
                },
                {
                    itemImageSrc: 'http://localhost/test_images/sixth.png',
                    thumbnailImageSrc: 'http://localhost/test_images/sixth.png',
                    alt: 'content 6',
                    title: 'Title 6'
                },
                {
                    itemImageSrc: 'http://localhost/test_images/seventh.png',
                    thumbnailImageSrc: 'http://localhost/test_images/seventh.png',
                    alt: 'content 7',
                    title: 'Title 7'
                },
                
               
            ];
        },

        getImages() {
            return Promise.resolve(this.getData());
        }
    };




  





  const galleriaClass = computed(() => {
      return ['custom-galleria', { fullscreen: fullScreen.value }];
  });
  const fullScreenIcon = computed(() => {
      return `pi ${fullScreen.value ? 'pi-window-minimize' : 'pi-window-maximize'}`;
  });



const getSeverity = (status) => {
    switch (status) {
        case 'UPDATE':
            return 'success';

        case 'NEWS':
            return 'warning';

        case 'PATCH':
            return 'danger';

        default:
            return null;
    }
};



const GetNewsService = {
        GetNewsData() {
            return [
                {
                    id: '1',
                    name: 'Update #101',
                    description: 'There was a update to the game for xyz',
                    image: 'bamboo-watch.jpg',
                    typeofupdate: 'UPDATE'
                },
                {
                    id: '2',
                    name: 'NEWS #102',
                    description: 'Tasdasdasdasdz',
                    image: 'blue-band.jpg',
                    typeofupdate: 'NEWS'
                },
                {
                    id: '3',
                    name: 'PATCH #103',
                    description: '1213123123',
                    image: '',
                    typeofupdate: 'PATCH'
                },
                {
                    id: '3',
                    name: 'PATCH #105',
                    description: 'mwhahaha aha ha ha ha ha ha sdak jklajskl asdaklja asdklaj caslk acasl ascaklmsa',
                    image: '',
                    typeofupdate: 'PATCH'
                },
                
            ];
        },

        GetNewsDataa() {
            return [
            {
                    id: '1',
                    name: 'Update #101',
                    description: 'There was a update to the game for xyz',
                    image: 'bamboo-watch.jpg',
                    typeofupdate: 'UPDATE'
                },
                
            ];
        },
      
        GetNewsSmall() {
            return Promise.resolve(this.GetNewsData().slice(0, 10));
        },

       
        GetTotalNews(){
            return this.GetNewsData().length;
        }

     
      }
   
const loadData = async () => {
  try {
   
    GetNewsService.GetNewsSmall().then((data) => (news_feed.value = data.slice(0, 9)));
    const data = await GetNewsService.GetTotalNews();
    if(data > 3){
      show_more.value = true;
      total_news.value = data;
    }else if(data == 0){
      show_more.value = false;
      total_news.value = false;
      default_data.value = [{id: '1', name: 'No News', description: 'Im sorry there is no news yet', image: '', typeofupdate: 'UPDATE'}];
    }else{
      show_more.value = false;      
    }
    
  } catch (error) {
    toast.add({ severity: 'error', summary: 'News', detail: "there was an error getting the news", life: 3000 });
  }
};
  

// true or false if the game is installed..
async function isGameInstalled() {
  try {
    const result = await invoke("is_game_installed", {});
    console.log("i made it here for success on invoke");
    console.log(result);
    return result.toString();
  } catch (err) {
    console.log("error for invoke");
    toast.add({
      severity: "error",
      summary: "Version Check",
      detail: "There was an error checking for game_install_config.json",
      life: 3000,
    });
    return false;
  }
}

// produce window selector for the game installation
async function promptGameInstallPath(current_version) {

  return new Promise((resolve, reject) => {
    invoke('select_directory', {})
      .then((result) => {
        // result will contain the selected directory path
        console.log(result);
        resolve(result); // resolve the Promise with the result
      })
      .catch((err) => {
        // handle the error
        console.error(err);
        reject(err); // reject the Promise with the error
      });
  });


  /*const installPath = prompt('Please enter the game installation path:');
  const gameInstallPath = {
    install_path: installPath
  };
  const version_detail = await requestVersionDetails(current_version);

  try {
    const result = await invoke("create_game_install", {
      params: {
        filepath: installPath,
        install_path: JSON.stringify(gameInstallPath),
        version: current_version,
        version_details: JSON.stringify(version_detail),
      },
    });
    return result.toString();
  } catch (err) {
    toast.add({ severity: 'error', summary: 'Version Check', detail: "There was an error checking promp game install", life: 8000 });
    return false;
  }*/
}


// create the inital setup files required for the game launcher
async function setupGameConfigLauncher(gameInstallPath,dir_path,current_version) {

return new Promise((resolve, reject) => {
  invoke('create_game_install', { 
      params: {
        game_install_path: gameInstallPath,
        dir_path: dir_path,
        version: current_version,
        
      },
    })
    .then((result) => {
      // result will contain the selected directory path
      console.log(result);
      resolve(result); // resolve the Promise with the result
    })
    .catch((err) => {
      // handle the error
      console.error(err);
      reject(err); // reject the Promise with the error
    });
});


/*const installPath = prompt('Please enter the game installation path:');
const gameInstallPath = {
  install_path: installPath
};
const version_detail = await requestVersionDetails(current_version);

try {
  const result = await invoke("create_game_install", {
    params: {
      filepath: installPath,
      install_path: JSON.stringify(gameInstallPath),
      version: current_version,
      version_details: JSON.stringify(version_detail),
    },
  });
  return result.toString();
} catch (err) {
  toast.add({ severity: 'error', summary: 'Version Check', detail: "There was an error checking promp game install", life: 8000 });
  return false;
}*/
}

// return the game install location json file
async function getGameInstallLocation() {

  return new Promise((resolve, reject) => {
    invoke('get_game_install', {})
      .then((result) => {
        // result will contain the selected directory path
        console.log(result);
        resolve(result); // resolve the Promise with the result
      })
      .catch((err) => {
        // handle the error
        console.error(err);
        reject(err); // reject the Promise with the error
      });
  });

}



// define a function to get the current version
async function requestVersion() {
  try {
    const client = await getClient();
    const { data } = await client.get(domain+'request_version');
    return data.version;
  } catch (error) {
    toast.add({ severity: 'error', summary: 'Version Check', detail: "There was an issue contacting the version server", life: 6000 });
    return false;
  }
}

// Define a function to retrieve the version details for a given version
async function requestVersionDetails(version) {
  try {
    const client = await getClient();
    const { data } = await client.get(`http://127.0.0.1:8090/request_version_details?version=${version}`);
    return data;
  } catch (error) {
    toast.add({ severity: 'error', summary: 'Version Check', detail: "There was an issue contacting the version details server", life: 6000 });
    return false;
  }
}

// Define a function to download a file for a given version and filename
async function downloadFile(url, filepath,file) {
  console.log(url);
  console.log(filepath);

  return new Promise((resolve, reject) => {
    invoke('download_me', { url: url,installPath:filepath })
      .then((result) => {
        // result will contain the selected directory path
        console.log(result);
        resolve(result); // resolve the Promise with the result
      })
      .catch((err) => {
        // handle the error
        //console.error(err);
        toast.add({ severity: 'error', summary: 'Version Download', detail: "file:"+file+" "+JSON.stringify(err), life: 32000 });
        reject(err); // reject the Promise with the error
      });
  });
}
// validate the system files
async function validate_files(rootPath,manifest) {
  
  try {
    const result = await invoke("validate_me", {
                  params: {
                    root_path: rootPath,
                    json_string: manifest,
                  },
      });
    console.log("Checking game files...");
    console.log(JSON.stringify(result));
    return result.toString();
  } catch (err) {
      console.log("Error checking game files...");
      console.log(err);
      toast.add({ severity: 'error', summary: 'Game files check', detail: "There was an error checking game files:"+err, life: 8000 });
  }
}


async function PlayGame(){
  let install_location = await getGameInstallLocation();
  console.log(install_location['game']);
  console.log("i am clicked");
  let demo = "D:\\steam\\steamapps\\common\\Pummel Party\\PummelParty.exe"
  invoke('start_game', {path:demo})
      .then((result) => {
        // result will contain the selected directory path
        console.log(result);
        
      })
      .catch((err) => {
        // handle the error
        console.error(err);
        
      });

}

// Define the main function to run the game installation/update process
async function runGameInstallation() {
  let liveVersion;
  let isNewInstall;
  let installPath;
  let isNewInstall_notify = false;
  let is_offline = false;
  const checkVersion = async () => {
    [liveVersion, isNewInstall] = await Promise.all([
      requestVersion(),
      isGameInstalled(),
    ]);

    if (!liveVersion) {
      is_offline = true;
      toast.add({ severity: 'warn', summary: 'Version Check', detail: "Trying to re-connect to update server", life: 8000 });
      setTimeout(checkVersion, 40000); // call checkVersion again after 30 seconds
      
    } else {
      if(is_offline){
        toast.add({ severity: 'success', summary: 'Version Check', detail: "Server Online woo :)", life: 8000 });
      }
      
      console.log(liveVersion);
      console.log("i am result for new install: "+isNewInstall);
      // false game_install_config does not exist.. full install with path 
      // true means game file exist validate the files and continue...
      // because it returns a string and not a bool look for string of true :| dont know how to convert types in crappy JS
      // and im too lazy to google right now will look in future...
      if(isNewInstall == "true"){
        let install_location = await getGameInstallLocation();
        console.log(install_location);
        console.log(install_location['game']);
        if (install_location['game'] && install_location['game_dir'] && install_location['version']){
          let manifest = await requestVersionDetails(liveVersion);
          let manifest_size = Object.keys(manifest);
          if (manifest_size.length == 0) {
            console.log("manifest empty");
            toast.add({ severity: 'error', summary: 'Version Check', detail: "Error with manifest", life: 8000 });
          } else {
            console.log(install_location['game_dir']);
            let file_check = await validate_files(install_location['game_dir'],JSON.stringify(manifest));
            let file_check_obj = JSON.parse(file_check);
            total_files.value = file_check_obj['total'];
            current_file.value = "validating files";
            // everything success perfect... show button
            if(total_files.value == 0){
                current_file.value = "File validation complete everything is upto date";
                setTimeout(() => {
                play_button.value = "play"
                }, 2000); // set the timeout to 5 seconds (5000 milliseconds)
                
                setTimeout(() => {
                current_file.value = '';
                }, 5000); // set the timeout to 5 seconds (5000 milliseconds)
            }else{
              // lets tell user how many files we need..
              current_file.value = "Files needing updated:"+total_files.value;
              for (let k in file_check_obj['missing']){
                let build_url = domain+"download?version="+liveVersion+"&filename="+k
                let game_install_path = install_location['game_dir']+"/"+k; 
                current_file.value = k;
                try {
                    let test = await downloadFile(build_url,game_install_path,k);
                    if (test === null) {
                      total_files.value = total_files.value - 1;
                      console.log("success");
                    } else {
                      console.log("failure");
                    }
                  } catch (error) {
                    toast.add({ severity: 'error', summary: 'Version Download', detail: "file:"+k+" error:"+error, life: 8000 });
                  }
                }
              for (let k in file_check_obj['mismatched']){
                let build_url = domain+"download?version="+liveVersion+"&filename="+k
                let game_install_path = install_location['game_dir']+"/"+k; 
                current_file.value = k;
                try {
                  let test = await downloadFile(build_url,game_install_path,k);
                  if (test === null) {
                    total_files.value = total_files.value - 1;
                    console.log("success");
                  } else {
                    console.log("failure");
                  }
                } catch (error) {
                  toast.add({ severity: 'error', summary: 'Version Download', detail: "file:"+k+" error:"+error, life: 8000 });
                }
              }
              if(total_files.value == 0){
                total_files.value = 0;
                current_file.value = "download has complete doing filecheck validation";
                file_check = await validate_files(install_location['game_dir'],JSON.stringify(manifest));
                file_check_obj = JSON.parse(file_check);
                let new_check = file_check_obj['total'];
                if(new_check == 0){
                    current_file.value = "everything upto date woo!";
                    setTimeout(() => {
                      current_file.value = '';
                    }, 5000); // set the timeout to 5 seconds (5000 milliseconds)
                }else{
                  console.log("does not match");
                }
              }else{
                console.log("something went wrong");
              }
            }
          }
        }else{
          toast.add({ severity: 'error', summary: 'Install Check', detail: "The Json file is corrupt or wrongly formatted", life: 8000 });
        }
       
        
      }else{
        console.log("my game config does not exist i must create and do a full install...");
        // obtain latest version manifest..
        let manifest = await requestVersionDetails(liveVersion);
        let manifest_size = Object.keys(manifest);
        let exe_path ="none";
        for (let key in manifest) {
          if (key.includes('.exe')) {
            console.log("i found the executable"+key)
            exe_path = key;
          }
        }
        
       

        if (manifest_size.length == 0) {
          console.log("manifest empty");
          toast.add({ severity: 'error', summary: 'Version Check', detail: "Error with manifest", life: 8000 });
        } else {
          installPath = await promptGameInstallPath(liveVersion);
          

          
          if(installPath && installPath.length > 1){
            // build full game path
            let full_game_path = installPath+"/"+exe_path
            // covert slashes to correct slashes
            full_game_path = full_game_path.replace(/\//g, "\\");
            // setup the file for reading game exe location + current version..
            let setup_game_config_file = await setupGameConfigLauncher(full_game_path,installPath,liveVersion);
            let file_check = await validate_files(installPath,JSON.stringify(manifest));
            //convert to object so i can see how many files need to be downloaded/updated
            let file_check_obj = JSON.parse(file_check);
            total_files.value = file_check_obj['total'];
            //download?version=v1-13-5&filename=test/bin/im_bina.txt
            for (let k in file_check_obj['missing']){
              let build_url = domain+"download?version="+liveVersion+"&filename="+k
              let game_install_path = installPath+"/"+k; 
              console.log("i am the total"+file_check_obj['total']);
              
              current_file.value = k;
              //let res = await downloadFile(build_url,game_install_path);
              //console.log(res);
              try {
                
                let test = await downloadFile(build_url,game_install_path,k);
                if (test === null) {
                  total_files.value = total_files.value - 1;
                  console.log("success");
                } else {
                  console.log("failure");
                }
              } catch (error) {
                toast.add({ severity: 'error', summary: 'Version Download', detail: "file:"+k+" error:"+error, life: 8000 });
              }
              //console.log(game_install_path);
              //console.log(build_url);
              //console.log(k);

            }
            for (let k in file_check_obj['mismatched']){
              let build_url = domain+"download?version="+liveVersion+"&filename="+k
              let game_install_path = installPath+"/"+k; 
              console.log("i am the total"+file_check_obj['total']);
              
              current_file.value = k;
              //let res = await downloadFile(build_url,game_install_path);
              //console.log(res);
              try {
                
                let test = await downloadFile(build_url,game_install_path,k);
                if (test === null) {
                  total_files.value = total_files.value - 1;
                  console.log("success");
                } else {
                  console.log("failure");
                }
              } catch (error) {
                toast.add({ severity: 'error', summary: 'Version Download', detail: "file:"+k+" error:"+error, life: 8000 });
              }
              //console.log(game_install_path);
              //console.log(build_url);
              //console.log(k);

            }
            if(total_files.value == 0){
              total_files.value = 0;
              current_file.value = "download has complete doing filecheck validation";
              file_check = await validate_files(installPath,JSON.stringify(manifest));
              file_check_obj = JSON.parse(file_check);
              let new_check = file_check_obj['total'];
              if(new_check == 0){
                  current_file.value = "everything upto date woo!";
                  setTimeout(() => {
                    current_file.value = '';
                  }, 5000); // set the timeout to 5 seconds (5000 milliseconds)
              }else{
                console.log("does not match");
              }
            }else{
              console.log("something went wrong");
            }
            
            
           
          }
          
        }
      }
      
    }
  }

  checkVersion(); 
}
  
  
  
  

onMounted(() => {
  
  //console.log(isGameInstalled());
  //console.log(isGameInstalled());
  //runGameInstallation();

  //test();
  //check_version();
  
  runGameInstallation();
  PhotoService.getImages().then((data) => (images.value = data));
  //bindDocumentListeners();
  //loadData();
  // setTimeout(() => {
    // document.querySelector('.fade-in').classList.add('active');
  // loadnews_feed();
    
    
  //   
  // }, 1000);
});
  
  </script>


<style>
@import 'primeflex/primeflex.css';
@import "primevue/resources/themes/lara-light-indigo/theme.css";    

.default_image{
 
  content: url("../assets/logo.png");
  background-repeat: no-repeat;

  
}

.fade-in {
  opacity: 0;
  transition: opacity 1s ease-in-out;
}

.fade-in.active {
  opacity: 1;
}

.fade-out {
  opacity: 1;
  transition: opacity 1s ease-in-out;
}

.fade-out.active {
  opacity: 0;
}

.p-avatar.p-avatar-xl {
    width: 10rem;
    height: 10rem;
    font-size: 10rem;
}

.p-dock {
    position: absolute;
    z-index: 1;
    /* display: flex; */
    justify-content: center;
    align-items: center;
    pointer-events: none;
}

.p-progressbar .p-progressbar-value {
  background-color: #22C55E !important;
}

.border {
  border-style: solid;
}

.custom-galleria.fullscreen {
    display: flex;
    flex-direction: column;
}
.custom-galleria .p-galleria-content {
    position: relative;
}
.custom-galleria .p-galleria-content .p-galleria-thumbnail-wrapper {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
}
.custom-galleria .p-galleria-thumbnail-items-container {
    width: 100%;
}
.custom-galleria-footer {
    display: flex;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.397);
    
    color: #ffffff;
    transform: translate(0,-20px);
}
.custom-galleria-footer > button {
    background-color: transparent;
    color: #ffffff;
    border: 0 none;
    border-radius: 0;
    margin: 0.2rem 0;
}
.custom-galleria-footer > button.fullscreen-button {
    margin-left: auto;
}
.custom-galleria-footer > button:hover {
    background-color: rgba(255, 255, 255, 0.1);
}

.custom-galleria .title-container > span {
    font-size: 0.9rem;
    padding-left: 0.829rem;

}
.custom-galleria .title-container > span.title {
    font-weight: bold;
}

.main_image {
  transform: translate(-10px,0px);
}
.side_image{
  transform: translate(-26px,0px);
}

.play_button{
  transform: translate(300px,0);
}

.im_bottom{
  position: relative;
  bottom: 0;
}

</style>

