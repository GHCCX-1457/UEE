<template>
  <n-el tag="div" class="box-main" :style="{
    width: getWidth(props.width),
    height: getHeight(), // 最大64px
    margin: props.margin
  }">
    <n-el tag="div" class="left">
    </n-el>
    <n-el tag="div" class="content">
    </n-el>
    <n-el tag="div" class="right">
    </n-el>
    <n-el tag="div" class="title">
      <slot>
        hz-title-2
      </slot>
    </n-el>
  </n-el>

</template>

<script setup>

// eslint-disable-next-line no-undef
const props = defineProps({
  width: {
    type: String,
    default: '100%'
  },
  margin: {
    type: String,
    default: '5px 5px 5px 5px' // 上右下左
  },
});

function getWidth(width) {
  return `calc(${width} - 2px - ${props.margin.split(' ')[1]} - ${props.margin.split(' ')[3]})`
}

function getHeight() {
  return '46px'
}

</script>

<style scoped lang="less">

.box-main{
  position: relative;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}

.left{
  position: absolute;
  left: 0;
  top: 0;
  width: 21px;
  height: 46px;
  background-image: url("@/assets/hz-title/2/left.png");
  background-repeat: no-repeat;
}

.content{
  position: absolute;
  left: 21px;
  top: 0;
  right: 39px;
  width: calc(100% - 41px);
  height: 46px;
  background-image: url("@/assets/hz-title/2/content.png");
  background-size:100% 100%;
}

.right{
  position: absolute;
  right: 0;
  top: 0;
  width: 20px;
  height: 46px;
  background-image: url("@/assets/hz-title/2/right.png");
  background-repeat: no-repeat;
}

.title{
  position: absolute;
  left: 21px;
  top: 0;
  width: calc(100% - 41px);
  height: 46px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  color: #fff;
  font-weight: bold;
  // 文字最大一行
  white-space: nowrap;
  overflow: hidden;
}

</style>