<template>
<body>
<div class="app-container">
  <div class="app-header">
    <div class="app-header-left">
      <span class="app-icon"></span>
      <p class="app-name">Vodka Launcher</p>
      <titlebar></titlebar>
    </div>
    <div class="app-header-right">
      <button class="profile-btn">
        <span>Username</span>
      </button>
    </div>
    <button class="messages-btn">
      <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-message-circle">
        <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z" /></svg>
    </button>
  </div>
  <div class="app-content">
    <div class="app-sidebar">
        <a v-if="play_button == 'update'" v-tooltip.right="{ value: `Files Downloading...<br>723 Mb 1.0 mb/s</br> 2 mins Left`, escape: true, class: 'custom-error' }" href="" class="app-sidebar-link">
          <ProgressSpinner style="width: 50px; height: 50px" strokeWidth="8" fill="var(--surface-ground)"
    animationDuration=".5s" aria-label="Custom ProgressSpinner" />
      </a>
      <a v-if="play_button == 'play'" class="app-sidebar-link">
      <i class="pi pi-caret-right" style="color:#1c1c2c;font-size:1.5rem"></i>
    </a>
      <a href="" class="app-sidebar-link active">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-home">
          <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z" />
          <polyline points="9 22 9 12 15 12 15 22" /></svg>
      </a>

      <a class="app-sidebar-link">
      <i class="pi pi-discord" style="color:#1c1c2c;font-size:1.5rem"></i>
      </a>
      <a class="app-sidebar-link">
      <i class="pi pi-question" style="color:#1c1c2c;font-size:1.5rem"></i>
      </a>     


      <a class="app-sidebar-link">
        <i class="pi pi-cog" style="color:#1c1c2c;font-size:1.5rem"></i>
      </a>
      <a class="app-sidebar-link">
      <i class="pi pi-sign-out" style="color:#1c1c2c;font-size:1.5rem"></i>
      </a>
    </div>
    <div class="projects-section">
      <div class="projects-section-line">
        <div class="projects-status">
        </div>
      </div>
      <div class="project-boxes jsGridView">
        <div class="project-box-wrapper">
               <Galleria ref="galleria" v-model:activeIndex="activeIndex" :value="images" :numVisible="5" containerStyle="width: 830px;" :containerClass="galleriaClass"
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
                               <span>{{ images[activeIndex].alt.substr(0, 75) + " ... read more" }}</span>
                           </span>
                           
                       </div>
                   </template>
               </Galleria>
<<<<<<< HEAD
               <div class=slogan>
                <Image src="./src/assets/patch.png" alt="Image" width="415" />
                <Image src="./src/assets/Mainte.png" alt="Image" width="415" />
               </div>

    </div>
  </div>
</div>
<div class="messages-section">
  <button class="messages-close">
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-x-circle">
      <circle cx="12" cy="12" r="10" />
      <line x1="15" y1="9" x2="9" y2="15" />
      <line x1="9" y1="9" x2="15" y2="15" /></svg>
  </button>
  <div class="projects-section-header">
    <p>Latest News</p>
  </div>
  <div class="messages">
    <div class="message-box">
      <div class="message-content">
        <div class="message-header">
          <div class="name">Title 1</div>
          <div class="star-checkbox">
            <input type="checkbox" id="star-1">
            <label for="star-1">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" /></svg>
            </label>
          </div>
        </div>
        <p class="message-line">
          I got your first assignment. It was quite good. 🥳 We can continue with the next assignment.
        </p>
        <p class="message-line time">
          Dec, 12
        </p>
      </div>
    </div>
    <div class="message-box">
      <div class="message-content">
        <div class="message-header">
          <div class="name">Title 2</div>
          <div class="star-checkbox">
            <input type="checkbox" id="star-2">
            <label for="star-2">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" /></svg>
            </label>
          </div>
        </div>
        <p class="message-line">
          Hey, can tell me about progress of project? I'm waiting for your response.
        </p>
        <p class="message-line time">
          Dec, 12
        </p>
      </div>
    </div>
    <div class="message-box">
      <div class="message-content">
        <div class="message-header">
          <div class="name">Title 3</div>
          <div class="star-checkbox">
            <input type="checkbox" id="star-3">
            <label for="star-3">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" /></svg>
            </label>
          </div>
        </div>
        <p class="message-line">
          Awesome! 🤩 I like it. We can schedule a meeting for the next one.
        </p>
        <p class="message-line time">
          Dec, 12
        </p>
      </div>
    </div>
    <div class="message-box">
      <div class="message-content">
        <div class="message-header">
          <div class="name">Title 4</div>
          <div class="star-checkbox">
            <input type="checkbox" id="star-4">
            <label for="star-4">
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-star">
                <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2" /></svg>
            </label>
          </div>
        </div>
        <p class="message-line">
          I am really impressed! Can't wait to see the final result.
        </p>
        <p class="message-line time">
          Dec, 11
          
        </p>
      </div>
    </div>
  </div>
</div>
</div>
</div>

</body>

=======
           </div>
           
           
           <div class="col-12">
             <div class="play_button" v-if="play_button == 'play'">
               <Button label="Play" icon="pi pi-play" severity="success" size="large" @click="PlayGame" />
             </div>
             <div class="play_button" v-if="play_button == 'failed'">
               <Button label="Failed to update click to retry" severity="danger" size="large" />
             </div>
             <div class="play_button pb-2" v-if="play_button == 'update'">
               <Button label="Updating" severity="warning" icon="pi pi-spinner" iconPos="left">
                 <span class="pi pi-spinner pi-spin"></span>  &nbsp Updating
                 
               </Button>
             </div>
           </div>
         
           
         
     </div>
     <div class="col-4 text-center">
       <div class="side_image">
        <Image :src="`${domain}/static/main.png`" alt="Image" width="580" />
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
   
   
   
>>>>>>> 567cc5129d93987a5352e1fca8637e80c67d998e
 </template>
 
 
 <script setup>
   import { useToast } from "primevue/usetoast";
   import { ref, onMounted, computed, defineExpose } from "vue";
   import { invoke } from "@tauri-apps/api/tauri";
   import { getClient, Body, ResponseType } from '@tauri-apps/api/http';
   import { appWindow } from "@tauri-apps/api/window";
   import titlebar from "../components/TitleBar2.vue"
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
                     itemImageSrc: domain+'/static/1.png',
                     thumbnailImageSrc: domain+'/static/1.png',
                     alt: 'this is the content of the news article we are updating servers to do xyz and we are doing much more maintanance tasks to achieve better performance across the service infrastrucutre ',
                     title: 'Title 1   '
                 },
                 {
                     itemImageSrc: domain+'/static/2.png',
                     thumbnailImageSrc: domain+'/static/2.png',
                     alt: 'content 2',
                     title: 'title 2   '
                 },
                 {
                     itemImageSrc: domain+'/static/3.png',
                     thumbnailImageSrc: domain+'/static/3.png',
                     alt: 'content 3',
                     title: 'title 3   '
                 },
                 
                 
                
             ];
         },
         getImages() {
             return Promise.resolve(this.getData());
         }
     }
 /*
   const PhotoService = {
         getData() {
             return [
                 {
                     itemImageSrc: 'http://127.0.0.1:8090/static/2000-1000.png',
                     thumbnailImageSrc: 'http://127.0.0.1:8090/static/2000-1000.png',
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
     };*/
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
     const { data } = await client.get(`${domain}/request_version_details?version=${version}`);
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
         //total_files = 0;
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


// function to iterate over the missing file object

async function missing_missmatched(liveVersion,file_check_obj,installPath){
  console.log(liveVersion);
  console.log(file_check_obj);
  console.log(installPath);
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
      
    }
  for (let k in file_check_obj['mismatched']){
      let build_url = domain+"download?version="+liveVersion+"&filename="+k
      let game_install_path = installPath+"/"+k; 
      console.log("i am the total"+file_check_obj['total']);
      
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

  return ("finished this function lets go");
}



 async function PlayGame(){
   let install_location = await getGameInstallLocation();
   console.log(install_location['game']);
  
   // live version we use install_location['game'] but for testing i use pummel party :) 
   let demo = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\Pummel Party\\PummelParty.exe"
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
       
       // false game_install_config does not exist.. full install with path 
       // true means game file exist validate the files and continue...
       // because it returns a string and not a bool look for string of true :| dont know how to convert types in crappy JS
       // and im too lazy to google right now will look in future...
       if(isNewInstall == "true"){
         let install_location = await getGameInstallLocation();
         console.log(install_location);
         console.log(install_location['game']);
         current_file.value = "Fetching patching details";
         if (install_location['game'] && install_location['game_dir'] && install_location['version']){
           
           let manifest = await requestVersionDetails(liveVersion);
           let manifest_size = Object.keys(manifest);
           if (manifest_size.length == 0) {
             play_button.value="failed";
             current_file.value = "";
             toast.add({ severity: 'error', summary: 'Version Check', detail: "Error with manifest", life: 8000 });
           } else {
             let file_check = await validate_files(install_location['game_dir'],JSON.stringify(manifest));
             let file_check_obj = JSON.parse(file_check);
             total_files.value = file_check_obj['total'];
             current_file.value = "validating files";

             while(total_files.value > 0){
                 console.log("im executing"+total_files);
                 let fun = await missing_missmatched(liveVersion,file_check_obj,install_location['game_dir']);
                 console.log(fun);
                }
             // everything success perfect... show button
             if(total_files.value == 0){
                 current_file.value = "File validation complete everything is upto date";
                 setTimeout(() => {
                 play_button.value = "play"
                 }, 2000); // set the timeout to 2 seconds (2000 milliseconds)
                 
                 setTimeout(() => {
                 current_file.value = '';
                 }, 5000); // set the timeout to 5 seconds (5000 milliseconds)
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
             current_file.value = "validating files";

             while(total_files.value > 0){
                 console.log("im executing"+total_files);
                 let fun = await missing_missmatched(liveVersion,file_check_obj,installPath);
                 console.log(fun);
                }
             // everything success perfect... show button
             if(total_files.value == 0){
                 current_file.value = "File validation complete everything is upto date";
                 setTimeout(() => {
                 play_button.value = "play"
                 }, 2000); // set the timeout to 2 seconds (2000 milliseconds)
                 
                 setTimeout(() => {
                 current_file.value = '';
                 }, 5000); // set the timeout to 5 seconds (5000 milliseconds)
             }


            
           }else{
            toast.add({ severity: 'error', summary: 'Install path', detail: "Not a valid install path", life: 8000 });
           }
           
         }
       }
       
     }
   }
   checkVersion(); 
 }
   
   
   
   
 onMounted(() => {
   
   
   runGameInstallation();
   PhotoService.getImages().then((data) => (images.value = data));
   
   //loadData();
   // setTimeout(() => {
     // document.querySelector('.fade-in').classList.add('active');
   // loadnews_feed();
     
     
   //   
   // }, 1000);
 });
   

 document.addEventListener('DOMContentLoaded', function () {
  var modeSwitch = document.querySelector('.mode-switch');

  modeSwitch.addEventListener('click', function () {                     document.documentElement.classList.toggle('dark');
    modeSwitch.classList.toggle('active');
  });
  
  var listView = document.querySelector('.list-view');
  var projectsList = document.querySelector('.project-boxes');
  
  listView.addEventListener('click', function () {
    gridView.classList.remove('active');
    listView.classList.add('active');
    projectsList.classList.remove('jsGridView');
    projectsList.classList.add('jsListView');
  });
  
  gridView.addEventListener('click', function () {
    gridView.classList.add('active');
    listView.classList.remove('active');
    projectsList.classList.remove('jsListView');
    projectsList.classList.add('jsGridView');
  });
  
  document.querySelector('.messages-btn').addEventListener('click', function () {
    document.querySelector('.messages-section').classList.add('show');
  });
  
  document.querySelector('.messages-close').addEventListener('click', function() {
    document.querySelector('.messages-section').classList.remove('show');
  });
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
{
  box-sizing: border-box;
}

:root {
  --app-container: #f3f6fd;
  --main-color: #1f1c2e;
  --secondary-color: #4A4A4A;
  --link-color: #1f1c2e;
  --link-color-hover: #c3cff4;
  --link-color-active: #fff;
  --link-color-active-bg: #1f1c2e;
  --projects-section: #fff;
  --message-box-hover: #fafcff;
  --message-box-border: #e9ebf0;
  --more-list-bg: #fff;
  --more-list-bg-hover: #f6fbff;
  --more-list-shadow: rgba(209, 209, 209, 0.4);
  --button-bg: #1f1c24;
  --search-area-bg: #fff;
  --star: #1ff1c2e;
  --message-btn: #fff;
}

.dark:root {
  --app-container: #1f1d2b;
  --app-container: #111827;
  --main-color: #fff;
  --secondary-color: rgba(255,255,255,.8);
  --projects-section: #1f2937;
  --link-color: rgba(255,255,255,.8);
  --link-color-hover: rgba(195, 207, 244, 0.1);
  --link-color-active-bg: rgba(195, 207, 244, 0.2);
  --button-bg: #1f2937;
  --search-area-bg: #1f2937;
  --message-box-hover: #243244;
  --message-box-border: rgba(255,255,255,.1);
  --star: #ffd92c;
  --light-font: rgba(255,255,255,.8);
  --more-list-bg: #2f3142;
  --more-list-bg-hover: rgba(195, 207, 244, 0.1);
  --more-list-shadow: rgba(195, 207, 244, 0.1);
  --message-btn: rgba(195, 207, 244, 0.1);
}

html, body {
  width: 100%;
  height: 100vh;
  margin: 0;
}

body {
  font-family: "DM Sans", sans-serif;
  overflow: hidden;
  display: flex;
  justify-content: center;
  background-color: var(--app-container);
}

button, a {
  cursor: pointer;
}

.app-container {
  width: 100%;
  display: flex;
  flex-direction: column;
  height: 100%;
  background-color: var(--app-container);
  transition: 0.2s;
  max-width: 1800px;
}
.app-container button, .app-container input, .app-container optgroup, .app-container select, .app-container textarea {
  font-family: "DM Sans", sans-serif;
}
.app-content {
  display: flex;
  height: 100%;
  overflow: hidden;
  padding: 16px 24px 24px 0;
}
.app-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 16px 24px;
  position: relative;
}
.app-header-left, .app-header-right {
  padding-top: 25px;
  display: flex;
  align-items: center;
}
.app-header-left {
  flex-grow: 1;
}
.app-header-right button {
  margin-left: 10px;
}
.app-icon {
  width: 26px;
  height: 2px;
  border-radius: 4px;
  background-color: var(--main-color);
  position: relative;
}
.app-icon:before, .app-icon:after {
  content: "";
  position: absolute;
  width: 12px;
  height: 2px;
  border-radius: 4px;
  background-color: var(--main-color);
  left: 50%;
  transform: translatex(-50%);
}
.app-icon:before {
  top: -6px;
}
.app-icon:after {
  bottom: -6px;
}
.app-name {
  color: var(--main-color);
  margin: 0;
  font-size: 20px;
  line-height: 24px;
  font-weight: 700;
  margin: 0 32px;
}

.mode-switch {
  background-color: transparent;
  border: none;
  padding: 0;
  color: var(--main-color);
  display: flex;
  justify-content: center;
  align-items: center;
}

.search-wrapper {
  border-radius: 20px;
  background-color: var(--search-area-bg);
  padding-right: 12px;
  height: 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 480px;
  color: var(--light-font);
  box-shadow: 0 2px 6px 0 rgba(136, 148, 171, 0.2), 0 24px 20px -24px rgba(71, 82, 107, 0.1);
  overflow: hidden;
}
.dark .search-wrapper {
  box-shadow: none;
}

.search-input {
  border: none;
  flex: 1;
  outline: none;
  height: 100%;
  padding: 0 20px;
  font-size: 16px;
  background-color: var(--search-area-bg);
  color: var(--main-color);
}
.search-input:placeholder {
  color: var(--main-color);
  opacity: 0.6;
}

.add-btn {
  color: #fff;
  background-color: var(--button-bg);
  padding: 0;
  border: 0;
  border-radius: 50%;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.notification-btn {
  color: var(--main-color);
  padding: 0;
  border: 0;
  background-color: transparent;
  height: 32px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.profile-btn {
  padding: 0;
  border: 0;
  background-color: transparent;
  display: flex;
  align-items: center;
  padding-left: 12px;
  border-left: 2px solid #ddd;
}
.profile-btn img {
  width: 32px;
  height: 32px;
  -o-object-fit: cover;
     object-fit: cover;
  border-radius: 50%;
  margin-right: 4px;
}
.profile-btn span {
  color: var(--main-color);
  font-size: 16px;
  line-height: 24px;
  font-weight: 700;
}

.page-content  {
  flex: 1;
  width: 100%;
}

.app-sidebar {
  padding: 40px 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.app-sidebar-link {
  color: var(--main-color);
  color: var(--link-color);
  margin: 16px 0;
  transition: 0.2s;
  border-radius: 50%;
  flex-shrink: 0;
  width: 40px;
  height: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.app-sidebar-link:hover {
  background-color: var(--link-color-hover);
  color: var(--link-color-active);
}
.app-sidebar-link.active {
  background-color: var(--link-color-active-bg);
  color: var(--link-color-active);
}

.projects-section {
  flex: 2;
  background-color: var(--projects-section);
  border-radius: 32px;
  padding: 0px 0px 0px 10px;
  overflow: hidden;
  height: 100%;
  display: flex;
  flex-direction: column;
}
.projects-section-line {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.projects-section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  color: var(--main-color);
}
.projects-section-header p {
  font-size: 24px;
  line-height: 32px;
  font-weight: 700;
  opacity: 0.9;
  margin: 0;
  color: var(--main-color);
}
.projects-section-header .time {
  font-size: 20px;
}

.projects-status {
  display: flex;
}

.item-status {
  display: flex;
  flex-direction: column;
  margin-right: 16px;
}
.item-status:not(:last-child) .status-type:after {
  content: "";
  position: absolute;
  right: 8px;
  top: 50%;
  transform: translatey(-50%);
  width: 6px;
  height: 6px;
  border-radius: 50%;
  border: 1px solid var(--secondary-color);
}

.status-number {
  font-size: 24px;
  line-height: 32px;
  font-weight: 700;
  color: var(--main-color);
}

.status-type {
  position: relative;
  padding-right: 24px;
  color: var(--secondary-color);
}

.view-actions {
  display: flex;
  align-items: center;
}

.view-btn {
  width: 36px;
  height: 36px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 6px;
  border-radius: 4px;
  background-color: transparent;
  border: none;
  color: var(--main-color);
  margin-left: 8px;
  transition: 0.2s;
}
.view-btn.active {
  background-color: var(--link-color-active-bg);
  color: var(--link-color-active);
}
.view-btn:not(.active):hover {
  background-color: var(--link-color-hover);
  color: var(--link-color-active);
}

.messages-section {
  flex-shrink: 0;
  padding-bottom: 32px;
  background-color: var(--projects-section);
  margin-left: 24px;
  flex: 1;
  width: 100%;
  border-radius: 30px;
  position: relative;
  overflow: auto;
  transition: all 300ms cubic-bezier(0.19, 1, 0.56, 1);
}
.messages-section .messages-close {
  position: absolute;
  top: 12px;
  right: 12px;
  z-index: 3;
  border: none;
  background-color: transparent;
  color: var(--main-color);
  display: none;
}
.messages-section.show {
  transform: translateX(0);
  opacity: 1;
  margin-left: 0;
}
.messages-section .projects-section-header {
  position: sticky;
  top: 0;
  z-index: 1;
  padding: 32px 24px 0 24px;
  background-color: var(--projects-section);
}

.message-box {
  border-top: 1px solid var(--message-box-border);
  padding: 16px;
  display: flex;
  align-items: flex-start;
  width: 100%;
}
.message-box:hover {
  background-color: var(--message-box-hover);
  border-top-color: var(--link-color-hover);
}
.message-box:hover + .message-box {
  border-top-color: var(--link-color-hover);
}
.message-box img {
  border-radius: 50%;
  -o-object-fit: cover;
     object-fit: cover;
  width: 40px;
  height: 40px;
}

.message-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}
.message-header .name {
  font-size: 16px;
  line-height: 24px;
  font-weight: 700;
  color: var(--main-color);
  margin: 0;
}

.message-content {
  padding-left: 16px;
  width: 100%;
}

.star-checkbox input {
  opacity: 0;
  position: absolute;
  width: 0;
  height: 0;
}
.star-checkbox label {
  width: 24px;
  height: 24px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.dark .star-checkbox {
  color: var(--secondary-color);
}
.dark .star-checkbox input:checked + label {
  color: var(--star);
}
.star-checkbox input:checked + label svg {
  fill: var(--star);
  transition: 0.2s;
}

.message-line {
  font-size: 14px;
  line-height: 20px;
  margin: 8px 0;
  color: var(--secondary-color);
  opacity: 0.7;
}
.message-line.time {
  text-align: right;
  margin-bottom: 0;
}

.project-boxes {
  margin: 0 -8px;
  overflow-y: auto;
}
.project-boxes.jsGridView {
  display: flex;
  flex-wrap: wrap;
}
.project-boxes.jsGridView .project-box-wrapper {
  width: 33.3%;
}
.project-boxes.jsListView .project-box {
  display: flex;
  border-radius: 10px;
  position: relative;
}
.project-boxes.jsListView .project-box > * {
  margin-right: 24px;
}
.project-boxes.jsListView .more-wrapper {
  position: absolute;
  right: 16px;
  top: 16px;
}
.project-boxes.jsListView .project-box-content-header {
  order: 1;
  max-width: 120px;
}
.project-boxes.jsListView .project-box-header {
  order: 2;
}
.project-boxes.jsListView .project-box-footer {
  order: 3;
  padding-top: 0;
  flex-direction: column;
  justify-content: flex-start;
}
.project-boxes.jsListView .project-box-footer:after {
  display: none;
}
.project-boxes.jsListView .participants {
  margin-bottom: 8px;
}
.project-boxes.jsListView .project-box-content-header p {
  text-align: left;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
.project-boxes.jsListView .project-box-header > span {
  position: absolute;
  bottom: 16px;
  left: 16px;
  font-size: 12px;
}
.project-boxes.jsListView .box-progress-wrapper {
  order: 3;
  flex: 1;
}

.project-box {
  --main-color-card: #dbf6fd;
  border-radius: 30px;
  padding: 16px;
  background-color: var(--main-color-card);
}
.project-box-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
  color: var(--main-color);
}
.project-box-header span {
  color: #4A4A4A;
  opacity: 0.7;
  font-size: 14px;
  line-height: 16px;
}
.project-box-content-header {
  text-align: center;
  margin-bottom: 16px;
}
.project-box-content-header p {
  margin: 0;
}
.project-box-wrapper {
  transition: 0.2s;
}

.project-btn-more {
  padding: 0;
  height: 14px;
  width: 24px;
  height: 24px;
  position: relative;
  background-color: transparent;
  border: none;
  flex-shrink: 0;
  /*&:after, &:before {
    content: '';
    position: absolute;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background-color: var(--main-color);
    opacity: .8;
    left: 50%;
    transform: translatex(-50%);
  }

  &:before { top: 0;}
  &:after { bottom: 0; }*/
}

.more-wrapper {
  position: relative;
}

.box-content-header {
  font-size: 16px;
  line-height: 24px;
  font-weight: 700;
  opacity: 0.7;
}

.box-content-subheader {
  font-size: 14px;
  line-height: 24px;
  opacity: 0.7;
}

.box-progress {
  display: block;
  height: 4px;
  border-radius: 6px;
}
.box-progress-bar {
  width: 100%;
  height: 4px;
  border-radius: 6px;
  overflow: hidden;
  background-color: #fff;
  margin: 8px 0;
}
.box-progress-header {
  font-size: 14px;
  font-weight: 700;
  line-height: 16px;
  margin: 0;
}
.box-progress-percentage {
  text-align: right;
  margin: 0;
  font-size: 14px;
  font-weight: 700;
  line-height: 16px;
}

.project-box-footer {
  display: flex;
  justify-content: space-between;
  padding-top: 16px;
  position: relative;
}
.project-box-footer:after {
  content: "";
  position: absolute;
  background-color: rgba(255, 255, 255, 0.6);
  width: calc(100% + 32px);
  top: 0;
  left: -16px;
  height: 1px;
}

.participants {
  display: flex;
  align-items: center;
}
.participants img {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  overflow: hidden;
  -o-object-fit: cover;
     object-fit: cover;
}
.participants img:not(:first-child) {
  margin-left: -8px;
}

.add-participant {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: none;
  background-color: rgba(255, 255, 255, 0.6);
  margin-left: 6px;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0;
}

.days-left {
  background-color: rgba(255, 255, 255, 0.6);
  font-size: 12px;
  border-radius: 20px;
  flex-shrink: 0;
  padding: 6px 16px;
  font-weight: 700;
}

.mode-switch.active .moon {
  fill: var(--main-color);
}

.messages-btn {
  border-radius: 4px 0 0 4px;
  position: absolute;
  right: 0;
  top: 58px;
  background-color: var(--message-btn);
  border: none;
  color: var(--main-color);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 4px;
  display: none;
}

@media screen and (max-width: 980px) {
  .project-boxes.jsGridView .project-box-wrapper {
    width: 50%;
  }

  .status-number, .status-type {
    font-size: 14px;
  }

  .status-type:after {
    width: 4px;
    height: 4px;
  }

  .item-status {
    margin-right: 0;
  }
}
@media screen and (max-width: 880px) {
  .messages-section {
    transform: translateX(100%);
    position: absolute;
    opacity: 0;
    top: 0;
    z-index: 2;
    height: 100%;
    width: 100%;
  }
  .messages-section .messages-close {
    display: block;
  }

  .messages-btn {
    display: flex;
  }
}
@media screen and (max-width: 720px) {
  .app-name, .profile-btn span {
    display: none;
  }

  .add-btn, .notification-btn, .mode-switch {
    width: 20px;
    height: 20px;
  }
  .add-btn svg, .notification-btn svg, .mode-switch svg {
    width: 16px;
    height: 16px;
  }

  .app-header-right button {
    margin-left: 4px;
  }
}
@media screen and (max-width: 520px) {
  .projects-section {
    overflow: auto;
  }

  .project-boxes {
    overflow-y: visible;
  }

  .app-sidebar, .app-icon {
    display: none;
  }

  .app-content {
    padding: 16px 12px 24px 12px;
  }

  .status-number, .status-type {
    font-size: 10px;
  }

  .view-btn {
    width: 24px;
    height: 24px;
  }

  .app-header {
    padding: 16px 10px;
  }

  .search-input {
    max-width: 120px;
  }

  .project-boxes.jsGridView .project-box-wrapper {
    width: 100%;
  }

  .projects-section {
    padding: 24px 16px 0 16px;
  }

  .profile-btn img {
    width: 24px;
    height: 24px;
  }

  .app-header {
    padding: 10px;
  }

  .projects-section-header p,
.projects-section-header .time {
    font-size: 18px;
  }

  .status-type {
    padding-right: 4px;
  }
  .status-type:after {
    display: none;
  }

  .search-input {
    font-size: 14px;
  }

  .messages-btn {
    top: 48px;
  }

  .box-content-header {
    font-size: 12px;
    line-height: 16px;
  }

  .box-content-subheader {
    font-size: 12px;
    line-height: 16px;
  }

  .project-boxes.jsListView .project-box-header > span {
    font-size: 10px;
  }

  .box-progress-header {
    font-size: 12px;
  }

  .box-progress-percentage {
    font-size: 10px;
  }

  .days-left {
    font-size: 8px;
    padding: 6px 6px;
    text-align: center;
  }

  .project-boxes.jsListView .project-box > * {
    margin-right: 10px;
  }

  .project-boxes.jsListView .more-wrapper {
    right: 2px;
    top: 10px;
  }
}
/* width */
::-webkit-scrollbar {
  width: 0px;
  border-radius: 20px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #f1f1f1; 
  border-radius: 20px;
}
 
/* Handle */
::-webkit-scrollbar-thumb {
  background: #888; 
  border-radius: 20px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555; 
  border-radius: 20px;
}
.slogan {
  display: flex;
}
 </style>