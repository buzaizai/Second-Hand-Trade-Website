<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
import show from '@/components/show'
export default {
  name: 'App',
  components: { show }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0px;
}
</style>
