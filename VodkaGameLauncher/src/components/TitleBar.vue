<script setup>
import { ref } from "vue";
import { invoke } from "@tauri-apps/api/tauri";
import { appWindow } from "@tauri-apps/api/window";

async function AppClose(){
    appWindow.close();
}


</script>

<template>
    <div data-tauri-drag-region class="titlebar">
      <div @click="AppClose" class="titlebar-button" id="titlebar-close" width="15" height="15">
        <svg class="white_cross" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="15" height="15">
          <path fill="#ffffff" d="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41z"></path>
        </svg>
      </div>
    </div>
  </template>

<style>
.white_cross {
  fill: #ffffff; /* white color in hex format */
}
</style>