<template>
  <div>
    <div>
      <el-row>
        <el-col :span='3' v-for="product in products" :key="product.product_id" :offset='2'>
          <el-card :body-style="{ padding: '0px' }" style="min-width: 200px; max-width: 200px;max-height: 350px;">
            <img :src='product.image_url'
                 class='image' alt="">
            <div style='padding: 14px; box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);height: 100px;margin-bottom: 10px;'>
              <span>{{ product.name }}</span>
              <div class='bottom clearfix'>
                <p>{{ product.price }}元</p>
                <el-button type='text' class='button' @click="deleteProduct(product.product_id)">删除  </el-button>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
    </div>
    <div>
      <el-pagination  :current-page="this.page" @current-change="handlePageChange" :page-size="8"  layout="prev, pager, next" :total="page_count">
      </el-pagination>
    </div>
  </div>
</template>

<style>
.time {
  font-size: 13px;
  color: #999
}

.bottom {
  margin-top: 13px;
  line-height: 12px
}

.button {
  padding: 0;
  float: right
}

.image {
  width: 100%;
  display: block
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: ''
}

.clearfix:after {
  clear: both
}
</style>
<script>
import axios from "axios";

export default {
  data() {
    return {
      products: [],
      page: 1,
      loading: false,
      page_count: 1,
    }
  },
  mounted() {
    this.loadProducts()
    this.countProducts()
  },
  methods: {
    loadProducts() {
      this.loading = true
      axios.get(`/api/mysell?page=${this.page}`)
        .then(response => {
          this.products = response.data.products
          this.loading = false
        })
        .catch(error => {
          this.$message.error(error)
          this.loading = false
        })
    },
    deleteProduct(productId) {
      axios.delete(`/api/delete_mysell/${productId}`)
        .then(response => {
          this.loadProducts(); // 删除成功后重新加载产品列表
          this.countProducts(); // 更新产品总数
          this.$message.success('产品删除成功');
        })
        .catch(error => {
          this.$message.error('产品删除失败');
        });
    },
    handlePageChange(newPage) {
      this.page = newPage;
      this.loadProducts();
    },
    countProducts() {
      // 假设通过异步请求获取到了商品总数
      axios.get(`/api/mysell/count`)
        .then(response => {
          this.page_count = response.data.page_count; // 将商品总数赋值给totalProducts
        })
        .catch(error => {
          this.$message.error(error);
        })
    },
  }

}
</script>
