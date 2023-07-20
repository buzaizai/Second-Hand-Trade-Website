<template>
  <div class="circle-container">
    <el-carousel indicator-position="outside">
      <el-carousel-item v-for="item in carouselItems" :key="item.id" style="border-radius: 10px;">
        <img :src="item.imageSrc" alt="carousel item">
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>
export default {
  data() {
    return {
      carouselItems: [
        {imageSrc: '../static/images/裤子1.webp', id: 1},
        {imageSrc: '../static/images/鞋子1.webp', id: 2},
        {imageSrc: '../static/images/衣服1.webp', id: 3},
        {imageSrc: '../static/images/衣服2.webp', id: 4}
      ]
    }
  }
}
</script>

<style>
.el-carousel__item h3 {
  color: #475669;
  font-size: 18px;
  opacity: 0.75;
  line-height: 300px;
  margin: 0;
}

.el-carousel__item:nth-child(2n) {
  background-color: #99a9bf
}

.el-carousel__item:nth-child(2n+1) {
  background-color: #d3dce6
}

.circle-container {
  width: 50%;
  /* 设置宽度为屏幕的百分之五十 */
  height: 50%;
  padding-top: 0;
  border-radius: 10px;
  margin: 0 auto;
  /* 水平居中 */
}</style>
