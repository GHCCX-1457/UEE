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
    <n-el tag="div" class="title">
      <slot name="title">
        内置标题
      </slot>
    </n-el>
    <n-el tag="div" class="box-content">
      <n-el tag="div">
        <slot  name="content">
          hz-box-6
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
  top: 33px;
  left: 0;
  width: 32px;
  height: calc(100% - 16px);
  background-image: url("@/assets/hz-box/6/left_line.png");
}

.box-right{
  position: absolute;
  top: 33px;
  right: 0;
  width: 44px;
  height: calc(100% - 16px);
  background-image: url("@/assets/hz-box/6/right_line.png");
}

.box-top{
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 32px;
  background: linear-gradient(to right, #053380, rgba(5, 51, 128, 0.0));
}

.box-bottom{
  position: absolute;
  bottom: 0;
  left: 32px;
  width: calc(100% - 64px);
  height: 9px;
  background-image: url("@/assets/hz-box/6/line_bottom.png");
}

.box-left-top{
  position: absolute;
  top: 0;
  left: 0;
  width: 32px;
  height: 29px;
  background-image: url("@/assets/hz-box/6/left_top.png");
  background-repeat: no-repeat;
}

.box-right-top{
  position: absolute;
  top: 0;
  right: 0;
  width: 44px;
  height: 36px;
  background-image: url("@/assets/hz-box/6/right_top.png");
  background-repeat: no-repeat;
}

.box-left-bottom{
  position: absolute;
  bottom: 0;
  left: 0;
  width: 32px;
  height: 9px;
  background-image: url("@/assets/hz-box/6/left_bottom.png");
  background-repeat: no-repeat;
}

.box-right-bottom{
  position: absolute;
  bottom: 0;
  right: 0;
  width: 44px;
  height: 9px;
  background-image: url("@/assets/hz-box/6/right_bottom.png");
  background-repeat: no-repeat;
}

.box-content{
  position: absolute;
  top: 32px;
  left: 10px;
  width: calc(100% - 20px);
  height: calc(100% - 35px);
}

.title{
  position: absolute;
  top: 0;
  left: 35px;
  width: 100%;
  height: 32px;
  line-height: 32px;
  font-size: 16px;
  color: #fff;
  font-weight: bold;
}


</style>