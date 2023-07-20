<template>
  <div class="login_container"  >
    <div class="login_box">
      <h3 style="margin-top: 0px;">登录</h3>
      <!-- 登录表单区域 -->
      <el-form size="mini" >
        <!-- 用户名 -->
        <el-form-item>
          <el-input placeholder="邮箱" v-model="email"></el-input>
        </el-form-item>
        <!-- 密码 -->
        <el-form-item>
          <el-input placeholder="密码" show-password v-model="password"></el-input>
        </el-form-item>
        <!-- 记住我 -->
        <el-form-item>
          <el-checkbox label="记住我" class="rememberMe" v-model="remember"></el-checkbox>
        </el-form-item>
        <!-- 登录按钮 -->
        <el-form-item>
          <el-button type="primary" @click="login">登录</el-button>
        </el-form-item>
        <el-link type="success" @click="toZhuCe">点我注册&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;</el-link>
        <text>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;</text>
        <el-link type="info" @click="toWangJi">忘记密码？</el-link>
      </el-form>
    </div>
    <div class="platform_text">
      二手交易平台
    </div>
    <div class="logo">
      <img src="../../static/images/logo2.png" alt="logo" width="400px">
    </div>
  </div>
</template>
<script>
import axios from 'axios'

export default {
  name: 'login',
  data() {
    return {
      email: '',
      password: '',
      remember: false
    }
  },
  methods: {
    async login() {
      // 表单验证
      if (this.email === '') {
        // 邮箱为空，弹出错误提示
        this.$message.error('邮箱不能为空')
        return
      }

      if (this.password === '') {
        // 密码为空，弹出错误提示
        this.$message.error('密码不能为空')
        return
      }
      try {
        // 发送登录请求给后端
        const response = await axios.post('/api/login', {
          email: this.email,
          password: this.password
        })

        // 处理登录响应
        if (response.data.success) {
          // 示例：跳转到首页
          this.$router.push('/')
        } else {
          // 登录失败，弹出错误提示
          this.$message.error(response.data.message)
        }
      } catch (error) {
        // 发生错误，弹出错误提示
        this.$message.error('登录失败，请稍后重试')
        console.error(error)
      }
    },
    toZhuCe() {
      this.$router.push({path: '/signup'})
    },
    toWangJi() {
      this.$router.push({path: '/forget'})
    }
  }

}
</script>
<style scoped>
.login_container {
  background-image: url('../../static/images/pic.jpg');
  background-repeat: no-repeat;
  background-size: 100% 100%;
  position: fixed;
  height: 100%;
  width: 100%;
}
.login_box {
  width: 290px;
  height: 300px;
  /* background-color: #fff; */
  background-color: white;
  border-radius: 5px;
  left:180%;
  top: 0%;
  margin-left: 70%;
  margin-top: 15%;
}
.platform_text {
  position: absolute;
  top: 50%;
  left: 27%;
  font-size: 55px;
  font-weight: bold;
  letter-spacing: 10px;
}
.logo {
  position: absolute;
  top: 30%;
  left: 25%;
}
.el-form {
  padding: 32px;
  bottom: 0;
  width: 100%;
  box-sizing: border-box;
}
.el-button {
  width: 100%;
}
.code {
  width: 45%;
}

</style>
