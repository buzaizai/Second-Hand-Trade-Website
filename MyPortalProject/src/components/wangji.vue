<template>
  <div class="login_container">
    <div class="login_box">
      <!-- 忘记密码表单区域 -->
      <el-form size="mini">
        <el-form-item>
          <el-input placeholder="邮箱" v-model="email"></el-input>
        </el-form-item>
        <el-form-item>
          <el-input placeholder="验证码" v-model="emailcode"></el-input>
          <el-button type="primary" @click="sendVerificationCode">发送验证码</el-button>
        </el-form-item>
        <!-- 新密码 -->
        <el-form-item>
          <el-input placeholder="新密码" show-password v-model="newpassword"></el-input>
        </el-form-item>
        <!-- 确认密码 -->
        <el-form-item>
          <el-input placeholder="确认密码" show-password v-model="confirmpassword"></el-input>
        </el-form-item>
        <!-- 已了解并同意平台规则 -->
        <el-form-item>
          <el-checkbox label="已了解并同意平台规则" class="rememberMe" v-model="agree"></el-checkbox>
        </el-form-item>
        <!-- 修改密码按钮 -->
        <el-form-item>
          <el-button type="primary" @click="changePassword" :disabled="!isPasswordMatch">修改密码</el-button>
        </el-form-item>
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
import axios from "axios";

export default {
  name: 'forgot-password',
  data() {
    return {
      email: '',
      emailcode: '',
      newpassword: '',
      confirmpassword: '',
      agree: false
    }
  },
  computed: {
    isPasswordMatch() {
      return this.newpassword === this.confirmpassword;
    }
  },
  methods: {
    async sendVerificationCode() {
      try {
        await axios.post('/api/send_email_code', { email: this.email });
        this.$message('验证码已发送，请检查你的邮箱');
      } catch (error) {
        console.error('发送邮件失败', error);
        this.$message.error('发送邮件失败，请稍后再试');
      }
    },
      async changePassword() {
    // 表单验证
    if (this.email === '') {
      this.$message.error('邮箱不能为空');
      return;
    }

    if (this.emailcode === '') {
      this.$message.error('验证码不能为空');
      return;
    }

    if (this.newpassword === '') {
      this.$message.error('新密码不能为空');
      return;
    }

    if (this.confirmpassword === '') {
      this.$message.error('确认密码不能为空');
      return;
    }

    if (!this.isPasswordMatch) {
      this.$message.error('新密码和确认密码不匹配');
      return;
    }

    if (!this.agree) {
      this.$message.error('请同意平台规则');
      return;
    }

    try {
      // 发送修改密码请求给后端
      const response = await axios.post('/api/change-password', {
        email: this.email,
        code: this.emailcode,
        newPassword: this.newpassword
      });

      // 处理修改密码响应
      if (response.data.success) {
        // 修改密码成功，可以进行页面跳转或其他操作
        this.$message.success('密码修改成功');
        this.$router.push('/login');
      } else {
        // 修改密码失败，弹出错误提示
        this.$message.error(response.data.message);
      }
    } catch (error) {
      // 发生错误，弹出错误提示
      this.$message.error('密码修改失败，请稍后重试');
      console.error(error);
    }
  }
  },

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
