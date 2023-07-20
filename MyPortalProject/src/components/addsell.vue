<template>
    <div>
        <el-form ref="form" :model="form" label-width="80px">
  <el-form-item label="商品名">
    <el-input v-model="form.name"></el-input>
  </el-form-item>
  <el-form-item label="成色">
    <el-select v-model="form.region" placeholder="请选择成色">
      <el-option label="四成" value="1"></el-option>
      <el-option label="五成" value="2"></el-option>
      <el-option label="六成" value="3"></el-option>
      <el-option label="七成" value="4"></el-option>
      <el-option label="八成" value="5"></el-option>
      <el-option label="九成" value="6"></el-option>
    </el-select>
  </el-form-item>
  <el-form-item label="单价">
    <el-input v-model="form.name"></el-input>
  </el-form-item>
  <el-form-item label="数量">
    <el-input v-model="form.name"></el-input>
  </el-form-item>
  <el-form-item label="商品详情">
    <el-input type="textarea" v-model="form.desc"></el-input>
  </el-form-item>
  <el-form-item label="分类">
    <el-select v-model="form.region" placeholder="请选择商品分类">
      <el-option label="数码科技" value="1"></el-option>
      <el-option label="鞋服佩饰" value="2"></el-option>
      <el-option label="书籍文具" value="3"></el-option>
      <el-option label="日常用品" value="4"></el-option>
      <el-option label="其它" value="5"></el-option>
    </el-select>
  </el-form-item>
  <el-form-item label="商品图片">
        <el-upload
          action="#"
          list-type="picture-card"
          :on-success="handleUploadSuccess"
          :before-upload="beforeUpload"
        >
          <i class="el-icon-plus"></i>
        </el-upload>
      </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="onSubmit">增加</el-button>
    <el-button @click="back">取消</el-button>
  </el-form-item>
</el-form>
    </div>
</template>
<script>
export default {
  data() {
    return {
      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
      }
    }
  },
  methods: {
    onSubmit() {
      console.log('submit!')
    },
    back() {
      window.history.back()
    },
    handleUploadSuccess(response, file, fileList) {
      // 图片上传成功后的处理逻辑
    },
    beforeUpload(file) {
      // 图片上传前的处理逻辑
    }
  }
}
</script>
