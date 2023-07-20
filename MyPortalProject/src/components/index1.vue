<template>
  <el-page-header @back="goBack" content>
    <template #content>
      <span style="font-size: 14px;">详情页面</span>
    </template>
  </el-page-header>
</template>
<script>
export default {
  methods: {
    goBack() {
      window.history.back()
    }
  }
}
</script>
