<template>
  <div>
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="商品名" prop="name">
        <el-input v-model="form.name" required></el-input>
      </el-form-item>
      <el-form-item label="成色" prop="condition">
        <el-select v-model="form.condition" placeholder="请选择成色" >
          <el-option label="四成" value="四成"></el-option>
          <el-option label="五成" value="五成"></el-option>
          <el-option label="六成" value="六成"></el-option>
          <el-option label="七成" value="七成"></el-option>
          <el-option label="八成" value="八成"></el-option>
          <el-option label="九成" value="九成"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="单价" prop="price">
        <el-input v-model="form.price"></el-input>
      </el-form-item>
      <el-form-item label="数量" prop="quantity">
        <el-input v-model="form.quantity"></el-input>
      </el-form-item>
      <el-form-item label="商品详情" prop="details">
        <el-input type="textarea" v-model="form.details"></el-input>
      </el-form-item>
      <el-form-item label="分类" prop="category">
        <el-select v-model="form.category" placeholder="请选择商品分类">
          <el-option label="数码科技" value="数码科技"></el-option>
          <el-option label="鞋服佩饰" value="鞋服佩饰"></el-option>
          <el-option label="书籍文具" value="书籍文具"></el-option>
          <el-option label="日常用品" value="日常用品"></el-option>
          <el-option label="其它" value="其它"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="商品图片">
        <el-upload
          action="#"
          list-type="picture-card"
          :on-success="handleUploadSuccess"
          :before-upload="beforeUpload">
          <i class="el-icon-plus"></i>
        </el-upload>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">更改</el-button>
        <el-button @click="back">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      delivery: false,
      image_url: '',
      productId: 0,
      productList: [],
      form: {
        name: '',
        condition: '',
        price: 0,
        quantity: 0,
        details: '',
        category: '',
      },
    }
  },
  created() {
    this.productId = this.$route.params.id;
    this.fetchData();
  },
  methods: {
    onSubmit() {
      const data = {
        image_url: this.image_url,
        quantity: this.form.quantity,
        price: this.form.price,
        details: this.form.details,
        category: this.form.category,
        condition: this.form.condition,
        name: this.form.name
      }

      axios.post(`/api/update_product/${this.productId}/`, data, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(response => {
          if (response.data.success) {
            // 成功更新商品信息后的操作，比如跳转到其他页面或显示成功提示
            this.$message.success(response.data.message);
          } else {
            // 更新失败的操作，比如显示错误提示
            this.$message.error(response.data.message);
          }
        })
        .catch(error => {
          this.$message.error('商品信息更新失败:', error);
        });
    },
    fetchData() {
      const productId = this.$route.params.id; // 获取路由参数中的product_id
      // 发送异步请求到后端，传递product_id，并获取数据
      // 这里使用axios作为示例，你可以根据自己的项目需求选择合适的方式发送请求
      axios.get(`/api/mysell/${productId}`)
        .then(response => {
          this.productList = response.data;
          // 将获取到的数据赋值给form对象
          const product = this.productList[0]; // 假设只获取第一个商品作为示例
          this.form.name = product.name;
          this.form.condition = product.condition;
          this.form.price = product.price;
          this.form.quantity = product.quantity;
          this.form.details = product.details;
          this.form.category = product.category;
        })
        .catch(error => {
          console.error(error);
        });
    },
    back() {
      window.history.back()
    },
    beforeUpload(file) {
      const formData = new FormData();
      formData.append('image', file);

      axios.post('/api/upload_image/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        }
      }).then(response => {
        if (response.data.path) {
          this.image_url = response.data.path;
          this.$message.success('图片上传成功');
        } else {
          this.$message.error('图片上传失败');
        }
      }).catch(error => {
        this.$message.error('图片上传失败:', error);
      });
    }
  }
}
</script>
