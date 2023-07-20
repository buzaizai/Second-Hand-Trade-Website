<template>
  <div>
    <el-row class='tac' style="display: flex;">
      <el-col :span='3'>
        <el-menu default-active='' class='el-menu-vertical-demo'>
          <el-menu-item v-for="category in categories" :key="category.id" :index="category.id" @click="handleCategoryClick(category.name)">
            <i :class="category.icon"></i>
            <span slot='title'>{{ category.name }}</span>
          </el-menu-item>
        </el-menu>
      </el-col>
    </el-row>
    <div>
      <el-row>
        <el-col :span='getColSpan' :class="{'center': getColSpan === 6}" v-for="product in products" :key="product.product_id" :offset='getColOffset'>
          <el-card :body-style="{ padding: '0px' }"  style="min-width: 200px; max-width: 200px;max-height: 350px">
            <img :src='product.image'
                 class='image' alt="">
            <div style='padding: 14px; box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);height: 100px;margin-bottom: 10px;'>
              <span>{{ product.name }}</span>
              <div class='bottom clearfix'>
                <p>{{ product.price }}元</p>
                <router-link :to="'/detail/' + product.product_id">
                  <el-button type="text" class="button">详情</el-button>
                </router-link>
                <el-button type="text" class="button"  @click="addToCart(product.product_id)">加入购物车</el-button>
              </div>
            </div>
          </el-card>
        </el-col>
      </el-row>
      <div style="display: flex; justify-content: center; position: fixed; bottom: 20px; left: 50%; transform: translateX(-50%);">
        <el-pagination  :current-page="page" @current-change="handlePageChange" :page-size="8"  layout="prev, pager, next" :total="page_count">
        </el-pagination>
      </div>
    </div>

  </div>
</template>

<style>

.center {
  display: flex;
  justify-content: center;
  align-items: center;
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
      selectedCategory: '', // 当前选中的分类
      products: [],
      page: 1,
      loading: false,
      page_count: 1,
      categories: [
        { id: '1', name: '数码科技', icon: 'el-icon-camera' },
        { id: '2', name: '鞋服佩饰', icon: 'el-icon-s-custom' },
        { id: '3', name: '书籍文具', icon: 'el-icon-s-management' },
        { id: '4', name: '日常用品', icon: 'el-icon-paperclip' },
        { id: '5', name: '其它', icon: 'el-icon-grape' },
      ],
    }
  },
  mounted() {
    this.loadProducts()
    this.countProducts()
  },
  methods: {
    addToCart(productId) {
      axios.get('/api/add_cart', { params: { id: productId } })
        .then(response => {
          if (response.data.error) {
            this.$message.error(response.data.error);
            return;
          }
          this.$message.success('加入购物车成功');
          // 加入购物车成功，可以根据需要进行提示或其他操作
        })
        .catch(error => {
          this.$message('已加入购物车');
        });
    },
    loadProducts() {
      this.loading = true
      axios.get(`/api/products?page=${this.page}&category=${this.selectedCategory}`)
        .then(response => {
          this.products = response.data.products
          this.loading = false
        })
        .catch(error => {
          this.$message.error(error)
          this.loading = false
        })
    },
    handlePageChange(newPage) {
      this.page = newPage;
      this.loadProducts();
    },
    countProducts() {
      // 假设通过异步请求获取到了商品总数
      axios.get(`/api/products/count?category=${this.selectedCategory}`)
        .then(response => {
          this.page_count = response.data.page_count; // 将商品总数赋值给totalProducts
        })
        .catch(error => {
          this.$message.error(error);
        })
    },
    handleCategoryClick(name) {
      this.selectedCategory = name
      this.page = 1 // 选择新的分类后，重置页码为1
      this.countProducts()
      this.loadProducts()
    },
  },
  computed: {
    pageCount() {
      const pageSize = 8; // 每页显示的商品数量
      return Math.ceil(this.page_count / pageSize); // 使用Math.ceil方法向上取整
    },
    getColSpan() {
      const productCount = this.products.length; // 当前商品数量
      if (productCount <= 4) {
        return 24 / productCount; // 动态计算每个 el-col 的 span 值
      } else {
        return 3; // 默认每个 el-col 的 span 值为 3
      }
    },
    getColOffset() {
      const productCount = this.products.length; // 当前商品数量
      if (productCount <= 4) {
        return 2; // 不需要偏移
      } else {
        return 2; // 默认偏移值为 0
      }
    },

  }
}
</script>
