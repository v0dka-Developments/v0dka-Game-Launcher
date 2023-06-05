<script setup>
import { ref } from "vue";
import { invoke } from "@tauri-apps/api/tauri";
import { appWindow } from "@tauri-apps/api/window";
import { useToast } from "primevue/usetoast";
import { relaunch } from '@tauri-apps/api/process';
const toast = useToast();

const showTemplate = () => {
    toast.add({ severity: 'info', summary: 'Do you want to exit Your Game or sign out?', detail: 'Proceed to confirm', group: 'bc' });
};

async function AppClose(){
    appWindow.close();
}
async function signout() {
  localStorage.removeItem("email");
  localStorage.removeItem("password");
  localStorage.setItem("autologin", "false");
  relaunch();
}

</script>

<template>
    <div data-tauri-drag-region class="titlebar">
      <div @click="showTemplate" class="titlebar-button" id="titlebar-close" width="15" height="15">
        <svg class="white_cross" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="15" height="15">
          <path fill="#ffffff" d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41z"></path>
        </svg>
      </div>
    </div>
    <Toast position="center" group="bc">
    <template #message="slotProps">
        <div class="flex flex-column align-items-center" style="flex: 1">
            <div class="text-center">
                <i class="pi pi-exclamation-triangle" style="font-size: 3rem"></i>
                <div class="font-bold text-xl my-3">{{ slotProps.message.summary }}</div>
            </div>
            <div class="flex gap-2">
                <Button severity="secondary" label="Sign Out" @click="signout()"></Button>
                <Button severity="secondary" label="Exit" @click="AppClose()"></Button>
            </div>
        </div>
    </template>
</Toast>
  </template>

<style>
.white_cross {
  fill: #ffffff; /* white color in hex format */
}
.titlebar {
  background-color: rgba(212, 187, 187, 0.075);
}
.titlebar-button:hover {
  background-color: rgba(255, 0, 0, 0.158);
}
</style>