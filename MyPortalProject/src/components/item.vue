<template>
    <el-row class='tac' style="display: flex;">
        <el-col :span='3'>
            <el-menu default-active='1' class='el-menu-vertical-demo' @open='handleOpen' @close='handleClose'>
                <el-menu-item index='1' @click="handleCategoryClick(1)">
                    <i class='el-icon-camera'></i>
                    <span slot='title'>数码科技</span>
                </el-menu-item>
                <el-menu-item index='2' @click="handleCategoryClick(2)">
                    <i class='el-icon-s-custom'></i>
                    <span slot='title'>鞋服佩饰</span>
                </el-menu-item>
                <el-menu-item index='3' @click="handleCategoryClick(3)">
                    <i class='el-icon-s-management'></i>
                    <span slot='title'>书籍文具</span>
                </el-menu-item>
                <el-menu-item index='4' @click="handleCategoryClick(4)">
                    <i class='el-icon-paperclip'></i>
                    <span slot='title'>日常用品</span>
                </el-menu-item>
                <el-menu-item index='5' @click="handleCategoryClick(5)">
                    <i class='el-icon-grape'></i>
                    <span slot='title'>其它</span>
                </el-menu-item>
            </el-menu>
        </el-col>
    </el-row>
</template>

<script>
export default {
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath)
    }
  }
}
</script>
