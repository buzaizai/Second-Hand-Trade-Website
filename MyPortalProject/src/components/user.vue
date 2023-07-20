<template>
  <div style=''>
    <div class='grid-content bg-purple-dark' style='margin-top: 0px;height: 50%;text-align: center;display: flex;flex-direction: column;'>
      <h4 style='margin-left: 0;text-align: left;'>用户名：{{username}}</h4>
    </div>
    <div style='display: inline-flex;'>
      <h3 style='white-space: nowrap;display: flex;margin-top: 25px;'>用户名：</h3>
      <el-input placeholder='修改后的用户名' v-model='input' style='margin-top: 20px;'>
      </el-input>

    </div>
    <div style='margin-top: 1%;'>
      <el-button type='primary' round @click="updateUsername">确认修改</el-button>
    </div>
    <div class='grid-content bg-purple-dark' style='margin-top: 2%;height: 50%;text-align: center;display: flex;flex-direction: column;'>
      <h4 style='margin-left: 0;text-align: left;'>手机号:{{phone}}</h4>
      <h4 style='margin-left: 0;text-align: left;'>Email:{{email}}</h4>
    </div>
  </div>
</template>

<style>
.el-row {
  margin-bottom: 20px;

  &:last-child {
    margin-bottom: 0
  }
}

.el-col {
  border-radius: 4px;
}

.bg-purple-dark {
  background: #99a9bf
}

.bg-purple {
  background: #d3dce6
}

.bg-purple-light {
  background: #e5e9f2
}

.grid-content {
  border-radius: 4px
}

.row-bg {
  padding: 10px ;
  background-color: #f9fafc
}
</style>

<script>
import axios from "axios";

export default {
  data() {
    return {
      phone: '',
      email: '',
      username: '',
      input: ''
    }
  },
  methods:{
    async getUserInfo() {
      try {
        const authToken = this.getCookieValue('authToken');
        const response = await axios.get(`/api/get_user`, {
          headers: {
            Authorization: `Bearer ${authToken}`
          }
        });
        this.phone = response.data.phone;
        this.email = response.data.email;
        this.username = response.data.username;
      } catch (error) {
        this.$message.error('获取用户信息失败:', error);
      }
    },
    updateUsername() {
      const newUsername = this.input; // 获取输入框中的新用户名
      const authToken = this.getCookieValue('authToken');
      // 发送修改用户名的请求
      axios.post('/api/update_username', { username: newUsername },
        {
          headers: {
            Authorization: `Bearer ${authToken}`
          }
        }
      )
        .then(response => {
          this.$message.success('用户名修改成功');
          this.username = newUsername; // 更新username的值以反映修改后的用户名
        })
        .catch(error => {
          this.$message.error('修改用户名失败:', error);
        });
    },
    getCookieValue(name) {
      const cookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith(name + '='));
      if (cookie) {
        return cookie.split('=')[1];
      }
      return null;
    }
  },
  mounted() {
    this.getUserInfo()
  }
}
</script>
