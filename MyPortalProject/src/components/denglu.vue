<template>
  <div class="login_container">
    <div class="login_box">
      <h3>登录</h3>
      <!-- 登录表单区域 -->
      <el-form size="mini">
        <!-- 手机号 -->
        <el-form-item>
          <el-input placeholder="手机号" v-model="phone"></el-input>
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
          <el-button type="primary" native-type="submit">登录</el-button>
        </el-form-item>
        <el-link type="success" @click="toZhuCe">点我注册&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;</el-link>
        <text>&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;</text>
        <el-link type="info" @click="toWangJi">忘记密码？</el-link>
      </el-form>
    </div>
    <div class="platform_text">
      二手交易平台
    </div>
  </div>
</template>
<script>
export default {
  name: 'denglu',
  data() {
    return {
      phone: '',
      password: '',
      remember: false
    }
  },
  methods: {async login() {
      // 表单验证
      if (this.phone === '') {
        // 手机号为空，弹出错误提示
        this.$message.error('手机号不能为空');
        return;
      }

      if (this.password === '') {
        // 密码为空，弹出错误提示
        this.$message.error('密码不能为空');
        return;
      }

      try {
        // 发送登录请求给后端
        const response = await axios.post('/api/login', {
          phone: this.phone,
          password: this.password
        });

        // 处理登录响应
        if (response.data.success) {
          // 登录成功，可以进行页面跳转或其他操作

          // 示例：跳转到首页
          this.$router.push('/');
        } else {
          // 登录失败，弹出错误提示
          this.$message.error(response.data.message);
        }
      } catch (error) {
        // 发生错误，弹出错误提示
        this.$message.error('登录失败，请稍后重试');
        console.error(error);
      }
    }
  },
  toZhuCe() {
    this.$router.push({path: '/signup'})
  },
  toWangJi() {
    this.$router.push({path: '/forget'})
  }
}
</script>
<style scoped>
.login_container {
  background-image: linear-gradient(-180deg, #0a081c 0%, #0e81a5 100%);
  /*background-image: url("../images/bg_login.png");*/
  background-repeat: no-repeat;
  background-size: cover;
  height: 100%;
}
.login_box {
  width: 290px;
  height: 280px;
  /* background-color: #fff; */
  background-color: #6e849cb3;
  border-radius: 5px;
  position: absolute;
  left:160%;
  top: 90%;
}
.el-form {
  padding: 32px;
  position: absolute;
  bottom: 0;
  width: 100%;
  box-sizing: border-box;
}
.el-button {
  width: 100%;
}
.platform_text {
  position: absolute;
  top: 50%;
  left: 50%;
  font-size: 24px;
  font-weight: bold;
}

.code {
  width: 45%;
}
.rememberMe {
  color: #fff;
}
</style>
