
<template>
  <n-config-provider :theme="theme">
    <div>
      <n-layout position="absolute">
        <n-layout-header style="height: 64px;" bordered>
          <hz-system-top :menu-options="menuOptions" :user-info="userInfo"></hz-system-top>

        </n-layout-header>
        <n-layout position="absolute" style="top: 64px; bottom: 32px" :native-scrollbar="false">
          <n-layout-content>
              <router-view></router-view>
          </n-layout-content>
        </n-layout>
        <n-layout-footer
            bordered
            position="absolute"
            style="height: 32px;justify-content: center;display: flex;align-items: center;"
        >
          <n-ellipsis :line-clamp="1">
            ©2023 Created by CCX
          </n-ellipsis>
        </n-layout-footer>
      </n-layout>
    </div>
  </n-config-provider>
</template>

<script setup>

import {theme} from "@/bean/config";
import HzSystemTop from "@/components/hz-system/Hz-System-Top.vue";
import {h, onMounted} from "vue";
import {RouterLink} from "vue-router";
import {NIcon} from "naive-ui";
//eslint-disable-next-line
import {HomeSharp,InformationCircle} from "@vicons/ionicons5";
import {getUserInfo} from "@/api/hz-system-api";
import {useMessage} from "naive-ui";

const message = useMessage();

let menuOptions = [
  {
    label: () => h(
        RouterLink,
        {
          to:{
            name: 'IndexPage',
            params: {
              lang: 'zh-CN'
            }
          }
        },
        { default: () => '首页' }
    ),
    key: 'hz-system-system-home',
    icon: () => h(NIcon, null, { default: () => h(HomeSharp) })
  },
  
  {
    label: () => h(
        RouterLink,
        {
          to:{
            name: 'CityCountPage',
            params: {
              lang: 'zh-CN'
            }
          }
        },
        { default: () => 'CityCount' }
    ),
    key: 'city_count',
    icon: () => h(NIcon, null, { default: () => h(InformationCircle) })
  },
    
  {
    label: () => h(
        RouterLink,
        {
          to:{
            name: 'PiciCountPage',
            params: {
              lang: 'zh-CN'
            }
          }
        },
        { default: () => 'PiciCount' }
    ),
    key: 'pici_count',
    icon: () => h(NIcon, null, { default: () => h(InformationCircle) })
  },
    
  {
    label: () => h(
        RouterLink,
        {
          to:{
            name: 'SchooldatePage',
            params: {
              lang: 'zh-CN'
            }
          }
        },
        { default: () => 'Schooldate' }
    ),
    key: 'schooldate',
    icon: () => h(NIcon, null, { default: () => h(InformationCircle) })
  },
    
  {
    label: () => h(
        RouterLink,
        {
          to:{
            name: 'ScoreCountPage',
            params: {
              lang: 'zh-CN'
            }
          }
        },
        { default: () => 'ScoreCount' }
    ),
    key: 'score_count',
    icon: () => h(NIcon, null, { default: () => h(InformationCircle) })
  },
    
  {
    label: () => h(
        RouterLink,
        {
          to:{
            name: 'XunlianshujuPage',
            params: {
              lang: 'zh-CN'
            }
          }
        },
        { default: () => 'Xunlianshuju' }
    ),
    key: 'xunlianshuju',
    icon: () => h(NIcon, null, { default: () => h(InformationCircle) })
  },
    
];

let userInfo = {
  name: 'HZ',
  avatar: require('../../assets/header.png'),
  desc: '一位全栈工程师'
};

// 生命周期 mounted
onMounted(() => {
  loadUserInfo()
});

// 获取个人信息
const loadUserInfo = () => {
  getUserInfo().then(res => {
      if (res.code === 200) {
        userInfo.name = res.data.username;
        userInfo.desc = res.data.email;
        console.log(userInfo);
      } else {
        message.error(res.msg);
      }
  });
};

</script>

<style lang="less" scoped>

</style>
    