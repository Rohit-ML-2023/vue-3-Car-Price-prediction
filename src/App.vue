<!-- <script setup> -->
// This starter template is using Vue 3 <script setup> SFCs
// Check out https://vuejs.org/api/sfc-script-setup.html#script-setup
// import HelloWorld from './components/HelloWorld.vue'
<!-- </script> -->

<template>
  <nav>
    <!-- <router-link to="/">Home</router-link> | -->
    <router-view to="/about">About</router-view> 
    <router-link to="/Prediction"> Prediction </router-link>
  </nav>
  <router-view/>
  <!-- <img alt="Vue logo" src="./assets/logo.png" />
  <HelloWorld msg="Hello Vue 3 + Vite" /> -->
</template>

<style>
body {
  background-image: 'Homepage bg1.png' 
   style="width:100%" ;
  /* background-size: cover; */
  background-attachment: fixed;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  font-weight: bold;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #0b59a6;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  font-size:40;
  color: #296aab;
}

nav a.router-link-exact-active {
  color: #0b0ea6;
}
</style>
