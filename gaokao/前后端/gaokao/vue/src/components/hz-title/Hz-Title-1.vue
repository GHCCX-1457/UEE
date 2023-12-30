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
        hz-title-1
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
  return '64px'
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
  width: 39px;
  height: 64px;
  background-image: url("@/assets/hz-title/1/left.png");
}

.content{
  position: absolute;
  left: 39px;
  top: 0;
  right: 39px;
  width: calc(100% - 467px);
  height: 64px;
  background-image: url("@/assets/hz-title/1/content.png");
  background-repeat:no-repeat;
  background-size:100% 100%;
}

.right{
  position: absolute;
  right: 0;
  top: 0;
  width: 428px;
  height: 64px;
  background-image: url("@/assets/hz-title/1/right.png");
}

.title{
  position: absolute;
  left: 39px;
  top: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  font-size: 24px;
  color: #fff;
  font-weight: bold;
  // 文字最大一行
  white-space: nowrap;
  overflow: hidden;
}

</style>