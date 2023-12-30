<template>
  <n-config-provider :theme="theme" class="wh100">
    <n-card class="wh100 center" :bordered="false">
      <n-el class="title">基于大数据技术的高考志愿填报推荐系统</n-el>
      <n-el tag="div" class="login-box">
        <n-form ref="loginFrom" class="login-from">
          <n-form-item class="center">
            <n-gradient-text :size="36" type="success"  :gradient="{
              from: 'rgba(48,106,246,0.88)',
              to: 'rgba(91,119,208,0.87)'}">
              登录
            </n-gradient-text>
          </n-form-item>
          <n-form-item label="用户名" required :label-style="{color: 'white'}">
            <n-input v-model:value="loginFromeData.username" placeholder="请输入用户名"/>
          </n-form-item>
          <n-form-item label="密码" required :label-style="{color: 'white'}">
            <n-input v-model:value="loginFromeData.password" type="password" show-password-on="mousedown" placeholder="请输入密码" />
          </n-form-item>
          <n-form-item class="center">
            <n-button type="info" @click="login">登录</n-button>
            <n-button type="warning" @click="toResigter">去注册</n-button>
          </n-form-item>
         
        </n-form>
      </n-el>
    </n-card>
  </n-config-provider>

</template>

<script setup>

import { theme} from "@/bean/config";
import {loginIn, logout} from "@/api/hz-system-api";
import router from "@/router";

import {onMounted, ref} from "vue";
import {useMessage} from "naive-ui";

const loginFromeData = ref({
  username: '',
  password: '',
});

const message = useMessage();

// 生命周期 mounted
onMounted(() => {
  logout();
});

const login = () => {
  localStorage.setItem('token', 'start_login');
  if(loginFromeData.value.username === ''|| loginFromeData.value.password === ''){
    message.error('用户名或密码不能为空');
    return;
  }
  loginIn(loginFromeData.value).then(res => {
      if (res.code == 200){
        message.success('登录成功');
        localStorage.setItem('token', res.data.access_token);
        toBigScreen();
      } else {
        message.error(res.msg);
        localStorage.setItem('token', 'login_fail')
      }
  }).catch(err => {
    message.error('登录失败',err);
  });
};

const toResigter = () => {
  console.log('toResigter');
  router.push({
    name: 'RegisterPage'
  });
};

const toBigScreen = () => {
  router.push({
    name: 'BigScreenPage'
  });
};

</script>

<style lang="less" scoped>

.wh100{
  width: 100%;
  height: 100%;
  background-image: url("../../assets/hz-bg/login_bg.png");
  background-size: 100% 100%;
}

.center{
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-box{
  width: 440px;
  height: 60%;
  display: flex;
  flex-direction: column;

  margin-top: 60px;
  margin-right: 800px;
  background-color: rgba(34, 45, 75, 0.3);
  border-radius: 10px;
  //边框
  border: 1.5px solid rgba(86, 104, 161, 0.5);

  align-items: center;


}

.login-from{
  width: 350px;
  height: 300px;
  margin-top: 30px;

}

.login-from .n-button{
  margin: 5px;
}
.title{
  font-size: 40px;
  color: #49f0fd;
  margin-bottom: 20px;
  //水平居中
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

}
</style>