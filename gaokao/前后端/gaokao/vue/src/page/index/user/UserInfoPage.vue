<template>
  <n-space vertical justify="center" style="margin-top: 50px">
    <n-el tag="div" class="form-box">
      <n-form
          ref="formRef"
          :model="userInfo"
          label-placement="top"
          :label-width="160"
          :disabled="updateDisabled"
      >
        <n-form-item label="用户名" path="inputValue">
          <n-input v-model:value="userInfo.username" placeholder="Input" />
        </n-form-item>
        <n-form-item label="邮箱" path="inputValue">
          <n-input v-model:value="userInfo.email" placeholder="Input" />
        </n-form-item>
        <n-form-item label="姓氏" path="inputValue">
          <n-input v-model:value="userInfo.first_name" placeholder="Input" />
        </n-form-item>
        <n-form-item label="名字" path="inputValue">
          <n-input v-model:value="userInfo.last_name" placeholder="Input" />
        </n-form-item>
        <n-form-item label="创建时间" path="inputValue">
          <n-input v-model:value="userInfo.date_joined" placeholder="Input" />
        </n-form-item>
        <n-form-item label="最后登录时间" path="inputValue">
          <n-input v-model:value="userInfo.last_login" placeholder="Input" />
        </n-form-item>
      </n-form>
      <n-space justify="center" style="margin-top: 20px">
        <n-button
            type="primary"
            :disabled="updateDisabled"
            @click="updateUserInfo"
        >
          保存
        </n-button>
        <n-button
            type="primary"
            :disabled="!updateDisabled"
            @click="updateDisabled = false"
        >
          编辑
        </n-button>
      </n-space>
    </n-el>
  </n-space>
</template>

<script setup>

import {onMounted, ref} from "vue";
import {getUserInfo, setUserInfo} from "@/api/hz-system-api";
import {useMessage} from "naive-ui";

const message = useMessage();

const updateDisabled = ref(true);
const userInfo = ref({
  username: 'HZ',
  email: '563161210@qq.com',
  date_joined: '2021-08-01T14:00:00.000Z',
  first_name: '',
  last_name: '',
  last_login: '2021-08-01T14:00:00.000Z',
});

// 生命周期 mounted
onMounted(() => {
  loadUserInfo()
});

// 获取个人信息
function loadUserInfo() {
  getUserInfo().then(res => {
    if (res.code === 200) {
      userInfo.value = res.data;
    } else {
      message.error(res.msg);
    }
  });
}

// 更新个人信息
function updateUserInfo() {
  message.success('更新成功');
  console.log(userInfo.value)
  setUserInfo(userInfo.value).then(res => {
    if (res.code === 200) {
      userInfo.value = res.data;
    } else {
      message.error(res.msg);
    }
  });
  updateDisabled.value = true;
}

</script>

<style lang="less" scoped>

@media screen and (max-width: 768px) {
  .form-box {
    width: 85%;
    margin: 0 auto;
  }
}

@media screen and (min-width: 768px) {
  .form-box {
    width: 50%;
    margin: 0 auto;
  }
}
</style>