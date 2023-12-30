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
    <n-el tag="div" class="box-title">
      <span>
        <slot name="title">
          内置标题
        </slot>
      </span>
    </n-el>
    <n-el tag="div" class="box-content">
      <n-el tag="div">
        <slot  name="content">
          hz-box-4
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
  top: 72px;
  left: 0;
  width: 124px;
  height: calc(100% - 111px);
  background-image: url("@/assets/hz-box/4/arrange_left.png");
}

.box-right{
  position: absolute;
  top: 72px;
  right: 0;
  width: 125px;
  height: calc(100% - 111px);
  background-image: url("@/assets/hz-box/4/arrange_right.png");
}

.box-top{
  position: absolute;
  top: 0;
  left: 124px;
  width: calc(100% - 249px);
  height: 29px;
  background-image: url("@/assets/hz-box/4/line_top.png");
}

.box-bottom{
  position: absolute;
  bottom: 0;
  left: 124px;
  width: calc(100% - 249px);
  height: 39px;
  background-image: url("@/assets/hz-box/4/line_bottom.png");
}

.box-left-top{
  position: absolute;
  top: 0;
  left: 0;
  width: 124px;
  height: 72px;
  background-image: url("@/assets/hz-box/4/left_top.png");
}

.box-right-top{
  position: absolute;
  top: 0;
  right: 0;
  width: 125px;
  height: 72px;
  background-image: url("@/assets/hz-box/4/right_top.png");
}

.box-left-bottom{
  position: absolute;
  bottom: 4px;
  left: 0;
  width: 124px;
  height: 35px;
  background-image: url("@/assets/hz-box/4/left_bottom.png");
  background-repeat: no-repeat;
}

.box-right-bottom{
  position: absolute;
  bottom: 4px;
  right: 0;
  width: 125px;
  height: 35px;
  background-image: url("@/assets/hz-box/4/right_bottom.png");
}

.box-content{
  position: absolute;
  top: 72px;
  left: 25px;
  width: calc(100% - 50px);
  height: calc(100% - 110px);
}

.box-title{
  position: absolute;
  top: 29px;
  width: 100%;
  height: 43px;
  display: flex;
  justify-content: center;
  align-items: center;

  span{
    font-size: 24px;
    color: #fff;
    font-weight: bold;
  }
}

</style>