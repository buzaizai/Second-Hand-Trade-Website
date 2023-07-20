<template>
  <div class="hello">
    <index2></index2>
    <slideshow></slideshow>
    <div style="height: 700px;display: flex;width: 100%;">
      <card style="margin-left:10%;display: flex;"></card>
    </div>
  </div>
</template>
<script>
export default {
  name: 'show',
  data() {
    return {
      msg: ''
    }
  }
}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
