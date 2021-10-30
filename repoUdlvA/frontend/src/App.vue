<template>
  <div id="app">
    <img src="./assets/Banner.jpg" class="rounded mx-auto d-block" alt="..." width="800" height="350" style="border:5px solid black">
    <img src="./assets/RUDLaVida.png" alt="UDLV">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
