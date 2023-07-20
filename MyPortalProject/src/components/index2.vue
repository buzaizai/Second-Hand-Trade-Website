<template>
  <div class="hello">
    <div v-if="isLoggedIn" style="display: inline-flex;">
      <img src="../../static/images/logo.png"
        style="max-width: 100%;height: auto;border-left: 0px; display: flex;align-items: center;">
        <el-input placeholder="请输入要搜索的内容" v-model="input" clearable style="margin-top: 15px;align-items: center;justify-content: center;">
          <i slot="suffix" class="el-icon-search" @click="search" style="margin-top: 15px;"></i>
        </el-input>
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" style="display: flex;align-items: center;">
        <el-menu-item index="1"><a href="/#/" style="text-decoration: none;">商城</a> </el-menu-item>
        <el-menu-item index="2"><a href="/#/cart" style="text-decoration: none;">我的购物车</a></el-menu-item>
        <el-menu-item index="3"><a href="/#/sell" style="text-decoration: none;">我要出售</a></el-menu-item>
        <el-menu-item index="4" ><a href="/#/user" style="text-decoration: none;">个人信息</a></el-menu-item>
        <el-menu-item index="5"><a href="/#/mysell" style="text-decoration: none;">我发布的商品</a></el-menu-item>
      </el-menu>
    </div>
    <div v-if="!isLoggedIn" style="display: inline-flex;">
      <img src="../../static/images/logo.png"
        style="max-width: 100%;height: auto;border-left: 0px; display: flex;align-items: center;">
        <el-input placeholder="请输入要搜索的内容" v-model="input" clearable style="margin-top: 15px;align-items: center;">
          <i slot="suffix" class="el-icon-search" @click="search" style="margin-top: 15px;"></i>
        </el-input>
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" style="display: flex;align-items: center;">
        <el-menu-item index="1"><a href="/#/" style="text-decoration: none;">商城</a></el-menu-item>
        <el-menu-item index="2"><a href="/#/signup" style="text-decoration: none;">注册</a></el-menu-item>
        <el-menu-item index="3"><a href="/#/login" style="text-decoration: none;">登录</a></el-menu-item>
      </el-menu>
    </div>
  </div>
</template>
<script>
export default {
  name: 'index2',
  data() {
    return {
      msg: '',
      input: '',
      isLoggedIn: true,
      activeIndex: ''
    }
  },
  methods: {
    search() {
      console.log('搜索')
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
}</style>
