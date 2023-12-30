<template>
  <n-el tag="div" class="box-main" :style="{
    width: getWidth(props.width),
    height: getHeight(props.height),
    margin: props.margin
  }"
  :class="props.showName === true ? 'map2' : 'map1'"
  >
    <n-el tag="div" class="content">
      <slot>
        hz-decoration-3
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
  height: {
    type: String,
    default: '100%'
  },
  margin: {
    type: String,
    default: '5px 5px 5px 5px' // 上右下左
  },
  showName: {
    type: Boolean,
    default: true
  },
});

function getWidth(width) {
  return `calc(${width} - 2px - ${props.margin.split(' ')[1]} - ${props.margin.split(' ')[3]})`
}

function getHeight(height) {
  return `calc(${height} - 2px - ${props.margin.split(' ')[0]} - ${props.margin.split(' ')[2]})`
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

.content{
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 24px;
  color: #fff;
  font-weight: bold;
  // 文字最大一行
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.map1{
  background-image: url("@/assets/hz-decoration/3/map0.png");
  background-size: 100% 100%;
  background-repeat: no-repeat;
}

.map2{
  background-image: url("@/assets/hz-decoration/3/map1.png");
  background-size: 100% 100%;
  background-repeat: no-repeat;
}

</style>