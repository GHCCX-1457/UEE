<template>
  <n-el tag="div" class="box-main" :style="{
    width: getWidth(props.width),
    height: getHeight(props.height),
    margin: props.margin
  }">
    <n-el tag="div" class="box-left" />
    <n-el tag="div" class="box-right" />
    <n-el tag="div" class="box-content">
      <slot>
        hz-box-3
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

.box-left{
  position: absolute;
  top: 0;
  left: 0;
  width: 22px;
  height: 22px;
  background-image: url("@/assets/hz-box/3/left_top.png");
}
.box-right{
  position: absolute;
  bottom: 0;
  right: 0;
  width: 22px;
  height: 22px;
  background-image: url("@/assets/hz-box/3/right_bottom.png");
}

.box-content {
  width: calc(100% - 22px);
  height: calc(100% - 22px);
  position: relative;
  margin: 10px;
}
</style>