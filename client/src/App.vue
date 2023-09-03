<script setup>
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
import SidebarComponent from './components/SideBar.vue'
import { RouterView } from 'vue-router'

</script>

<template>
  <div class="app-container">
    <SidebarComponent />
    <router-view class="content-view" />
  </div>
</template>

<style>
.app-container {
  display: flex;
  height: 100vh;  /* Utilise toute la hauteur de la fenêtre */
}
.content-view {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
}
</style>
