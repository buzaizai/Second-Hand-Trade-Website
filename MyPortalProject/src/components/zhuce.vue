<template>
  <div class="login_container">
    <div class="login_box">
      <!-- 注册表单区域 -->
      <el-form size="mini" ref="registerForm">
        <el-form-item>
          <el-input placeholder="手机号码" v-model="phone"></el-input>
        </el-form-item>
        <el-form-item>
          <el-input placeholder="邮箱" v-model="email"></el-input>
        </el-form-item>
        <!-- 用户名 -->
        <el-form-item>
          <el-input placeholder="验证码" v-model="emailCode"></el-input><el-button type="primary" @click="sendEmailCode">发送验证码</el-button>
        </el-form-item>
        <!-- 密码 -->
        <el-form-item>
          <el-input placeholder="密码" show-password v-model="password"></el-input>
        </el-form-item>
        <!-- 记住我 -->
        <el-form-item>
          <el-checkbox label="已了解并同意平台规则" class="rememberMe"></el-checkbox>
        </el-form-item>
        <!-- 登录按钮 -->
        <el-form-item>
          <el-button type="primary" @click="register">注册</el-button>
        </el-form-item>
      </el-form>
      <div class="platform_text">
        二手交易平台
      </div>
      <div class="logo">
        <img src="../../static/images/logo2.png" alt="logo" width="400px">
      </div>
    </div>
  </div>
</template>
<script>
import axios from 'axios'
export default {
  name: 'login',
  data() {
    return {
      phone: '',
      email: '',
      emailCode: '',
      password: '',
    }
  },
  methods: {
    toZhuCe() {
      this.$router.push({path: '/signup'})
    },
    toWangJi() {
      this.$router.push({path: '/forget'})
    },
      async sendEmailCode() {
    try {
      await axios.post('/api/send_email_code', { email: this.email });
      this.$message('验证码已发送，请检查你的邮箱');
    } catch (error) {
      console.error('发送邮件失败', error);
      this.$message.error('发送邮件失败，请稍后再试');
    }
  },
    register() {
      const data = {
        phone: this.phone,
        email: this.email,
        emailCode: this.emailCode,
        password: this.password
      }
      axios.post('http://localhost:8000/api/register', data, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
        .then(response => {
          if (response.data.success) {
            this.$message('注册成功!')
            window.location.href = '/#/login'
          } else {
            this.$message.error('注册失败：' + response.data.error)
          }
        })
        .catch(error => {
          this.$message.error('请求失败：' + error)
        })
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
  height: 350px;
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
