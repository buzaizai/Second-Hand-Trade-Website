<template>
    <div class="card" style="margin-left: 20%;">
      <el-card class="box-card" :body-style="{ display: 'flex',width: '100%'}">
        <div class="left">
          <img :src="imgSrc" alt="图片" class="img">
        </div>
        <div class="right">
          <div class="showSpace">
            <div>
              <label>商品名：</label>
            </div>
            <div>
              <label>成色：</label>
            </div>
            <div>
              <label>数量：</label>
            </div>
            <div>
              <label>单价：</label>
            </div>
            <div>
              <label>详情：</label>
            </div>
            <div>
              <label>分类：</label>
            </div>
          </div>
        </div>
      </el-card>
    </div>
  </template>
<script>
export default {
  name: 'card',
  data() {
    return {}
  },
  props: {
    imgSrc: {
      type: String
    },
    form: {
      type: Object
    }
  }
}
</script>
  <style>
  .img{
    width: 100%;
    height: 100%;
    overflow: hidden;
  }
  .box-card{
    height: 50vh;
    width: 50vw;
    display: flex;
    flex-direction: row;
  }
  .left{
    width: 50%;
    padding: 12% 5%;
    margin: 0 auto;
  }
  .right{
    width: 50%;
    padding: 10% 0;
  }
  .showSpace{
    justify-content: left;
  }
  .showSpace>div{
    margin: 20px 0;
    margin-right: 30%;
  }
  </style>
