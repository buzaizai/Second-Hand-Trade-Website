<template>
  <div>
    <el-form ref="form" :model="form" label-width="80px">
      <el-form-item label="商品名" prop="name">
        <el-input v-model="name" required></el-input>
      </el-form-item>
      <el-form-item label="成色" prop="condition">
        <el-select v-model="condition" placeholder="请选择成色" >
          <el-option label="四成" value="四成"></el-option>
          <el-option label="五成" value="五成"></el-option>
          <el-option label="六成" value="六成"></el-option>
          <el-option label="七成" value="七成"></el-option>
          <el-option label="八成" value="八成"></el-option>
          <el-option label="九成" value="九成"></el-option>
        </el-select>
      </el-form-item>
      <el-form-item label="单价" prop="price">
        <el-input v-model="price"></el-input>
      </el-form-item>
      <el-form-item label="数量" prop="quantity">
        <el-input v-model="quantity"></el-input>
      </el-form-item>
      <el-form-item label="商品详情" prop="detail">
        <el-input type="textarea" v-model="details"></el-input>
      </el-form-item>
      <el-form-item label="分类" prop="category">
        <el-select v-model="category" placeholder="请选择商品分类">
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
        <el-button type="primary" @click="onSubmit">发布</el-button>
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
      name: '',
      delivery: false,
      quantity: 0,
      price: 0,
      details: '',
      category: '',
      condition: '',
      image_url: ''
    }
  },
  methods: {
    onSubmit() {
      const data ={
        image_url: this.image_url,
        quantity: this.quantity,
        price: this.price,
        details: this.details,
        category: this.category,
        condition: this.condition,
        name: this.name
      }
      axios.post('/api/add_product',  data, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(response => {
          const productId = response.data.product_id;

          axios.post('/api/add_mysell', { id: productId },
            {
              headers: {
                'Content-Type': 'application/json'
              }
            }
          )
            .then(() => {
              this.$router.push('/mysell')
            })
            .catch(error => {
              this.$message.error('导入mysell表失败:', error);
            });
        })
        .catch(error => {
          this.$message.error('保存到Product表失败:', error);
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
