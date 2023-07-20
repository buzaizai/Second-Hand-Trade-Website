<template>
  <div>
    <index2></index2>
    <index1></index1>
    <div class="card" style="margin-left: 20%;height: 70%">
      <el-card class="box-card" :body-style="{ display: 'flex',width: '100%'}" style="height: 70vh">
        <div class="left">
          <img :src="product.image_url" alt="图片" class="img">
        </div>
        <div class="right">
          <div class="showSpace" style="margin-top: 0">
            <div>
              <label>商品名：</label>
              <span>{{ product.name }}</span>
            </div>
            <div>
              <label>成色：</label>
              <span>{{ product.condition }}</span>
            </div>
            <div>
              <label>数量：</label>
              <span>{{ product.quantity }}</span>
            </div>
            <div>
              <label>单价：</label>
              <span>{{ product.price }}</span>
            </div>
            <div>
              <label>详情：</label>
              <span>{{ product.details }}</span>
            </div>
            <div>
              <label>分类：</label>
              <span>{{ product.category }}</span>
            </div>
          </div>
        </div>
      </el-card>
    </div>
  </div>
</template>
<script>
import axios from "axios";

export default {
  name: 'card',
  data() {
    return {
      productId: '',
      product: {}
    }
  },
  created() {
    this.productId = this.$route.params.productId;
  },
  props: {
    imgSrc: {
      type: String
    },
    form: {
      type: Object
    }
  },
  methods: {
     getProduct() {
      axios.get(`/api/product?id=${this.productId}`)
        .then(response => {
          this.product = response.data;
        })
        .catch(error => {
          this.$message.error(error);
        });
    }
  },
    mounted() {
    this.getProduct();
  },
}
</script>
  <style>
  .img{
    width: 100%;
    height: 100%;
    overflow: hidden;
  }
  .box-card{
    height: 70vh;
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
