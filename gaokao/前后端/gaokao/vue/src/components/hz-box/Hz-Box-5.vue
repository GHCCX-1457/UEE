<template>
  <n-el tag="div" class="box-main" :style="{
    width: getWidth(props.width),
    height: getHeight(props.height),
    margin: props.margin
  }">
    <n-el tag="div" class="box-top">
    </n-el>
    <n-el tag="div" class="box-bottom">
    </n-el>
    <n-el tag="div" class="box-left">
    </n-el>
    <n-el tag="div" class="box-right">
    </n-el>
    <n-el tag="div" class="box-left-top">
    </n-el>
    <n-el tag="div" class="box-right-top">
    </n-el>
    <n-el tag="div" class="box-left-bottom">
    </n-el>
    <n-el tag="div" class="box-right-bottom">
    </n-el>
    <n-el tag="div" class="box-content">
      <n-el tag="div">
        <slot  name="content">
          hz-box-5
        </slot>
      </n-el>
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
  top: 8px;
  left: 0;
  width: 24px;
  height: calc(100% - 16px);
  background-image: url("@/assets/hz-box/5/line_left.png");
}

.box-right{
  position: absolute;
  top: 8px;
  right: 0;
  width: 22px;
  height: calc(100% - 16px);
  background-image: url("@/assets/hz-box/5/line_right.png");
}

.box-top{
  position: absolute;
  top: 0;
  left: 22px;
  width: calc(100% - 44px);
  height: 8px;
  background-image: url("@/assets/hz-box/5/line_top.png");
}

.box-bottom{
  position: absolute;
  bottom: 0;
  left: 22px;
  width: calc(100% - 44px);
  height: 8px;
  background-image: url("@/assets/hz-box/5/line_bottom.png");
}

.box-left-top{
  position: absolute;
  top: 0;
  left: 0;
  width: 24px;
  height: 8px;
  background-image: url("@/assets/hz-box/5/left_top.png");
  background-repeat: no-repeat;
}

.box-right-top{
  position: absolute;
  top: 0;
  right: 0;
  width: 22px;
  height: 8px;
  background-image: url("@/assets/hz-box/5/right_top.png");
  background-repeat: no-repeat;
}

.box-left-bottom{
  position: absolute;
  bottom: 0;
  left: 0;
  width: 22px;
  height: 8px;
  background-image: url("@/assets/hz-box/5/left_bottom.png");
  background-repeat: no-repeat;
}

.box-right-bottom{
  position: absolute;
  bottom: 0;
  right: 0;
  width: 22px;
  height: 8px;
  background-image: url("@/assets/hz-box/5/right_bottom.png");
  background-repeat: no-repeat;
}

.box-content{
  position: absolute;
  top: 8px;
  left: 8px;
  width: calc(100% - 16px);
  height: calc(100% - 16px);
}


</style>