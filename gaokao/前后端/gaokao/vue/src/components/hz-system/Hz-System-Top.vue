<template>
  <n-config-provider :theme="theme">
    <n-layout>
      <n-el tag="div" class="top-box">
        <n-el tag="div" class="top-box-logo">
          <n-gradient-text :size="24" type="success">
            HZ
          </n-gradient-text>
        </n-el>
        <n-el tag="div" class="top-box-main">
          <n-el tag="div" class="top-box-user">
            <n-gradient-text :size="24" type="success">
              <n-menu mode="horizontal" :options="props.menuOptions" @update:value="handleUpdateValue"/>
            </n-gradient-text>
          </n-el>
          <n-el tag="div" class="top-box-user">
            <n-space>
              <n-switch
                  v-model:value="isDark"
                  @update:value="switchTheme"
                  class="switch-theme"
              >
                <template #checked-icon>
                  <n-icon :component="Moon"/>
                </template>
                <template #unchecked-icon>
                  <n-icon :component="Sunny"/>
                </template>
              </n-switch>
              <n-dropdown trigger="hover" :options="options" @select="handleSelect">
                <n-icon :component="Apps" size="24"/>
              </n-dropdown>
            </n-space>
          </n-el>
        </n-el>
      </n-el>
    </n-layout>
  </n-config-provider>
</template>

<script setup>
import {isDark, switchTheme, theme} from "@/bean/config";
import {Apps, Exit, HomeSharp, Moon, Sunny} from "@vicons/ionicons5";
import {h} from "vue";
import {RouterLink} from "vue-router";
import {NIcon,NAvatar,NText} from "naive-ui";

const handleUpdateValue = (key,item) => {
  console.log(key,item);
};

const options = [
  {
    key: 'header',
    type: 'render',
    render: () => h(
        "div",
        {
          style: "display: flex; align-items: center; padding: 8px 12px;"
        },
        [
          h(NAvatar, {
            round: true,
            style: "margin-right: 12px;",
            src: props.userInfo.avatar
          }),
          h("div", null, [
            h("div", null, [h(NText, { depth: 2 }, { default: () => props.userInfo.name })]),
            h("div", { style: "font-size: 12px;" }, [
              h(
                  NText,
                  { depth: 3 },
                  { default: () => props.userInfo.desc }
              )
            ])
          ])
        ]
    )
  },
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
    key: 'hz-system-system-index',
    icon: () => h(NIcon, null, { default: () => h(HomeSharp) })
  },
  {
    label: () => h(
        RouterLink,
        {
          to:{
            name: 'UserInfoPage',
            params: {
              lang: 'zh-CN'
            }
          }
        },
        { default: () => '个人中心' }
    ),
    key: 'hz-system-system-user-info',
    icon: () => h(NIcon, null, { default: () => h(HomeSharp) })
  },
  {
    label: () => h(
        RouterLink,
        {
          to:{
            name: 'BigScreenPage',
            params: {
              lang: 'zh-CN'
            }
          }
        },
        { default: () => '返回大屏' }
    ),
    key: 'hz-system-big-screen',
    icon: () => h(NIcon, null, { default: () => h(HomeSharp) })
  },
  {
    label: () => h(
        RouterLink,
        {
          to:{
            name: 'LoginPage',
            params: {
              lang: 'zh-CN'
            }
          }
        },
        { default: () => '退出系统' }
    ),
    key: 'hz-system-system-exit',
    icon: () => h(NIcon, null, { default: () => h(Exit) })
  },
];

const handleSelect = (key) => {
  console.log(key);
};

// eslint-disable-next-line no-undef
const props = defineProps({
  menuOptions: {
    type: Array,
    default: () => []
  },
  userInfo: {
    type: Object,
    default: () => {}
  }
});



</script>

<style lang="less" scoped>

.top-box{
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 10px;
}

.top-box-logo{
  width: 10%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.top-box-main{
  width: 90%;
  height: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.switch-theme {
  font-size: 14px;
  color: #fff;
}

.top-box-user {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: row;
}
</style>