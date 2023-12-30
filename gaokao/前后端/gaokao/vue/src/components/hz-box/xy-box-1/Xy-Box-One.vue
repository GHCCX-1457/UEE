<template>
  <n-el tag="div"  class="box-main" :style="{
    width: getWidth(props.width),
    height: getHeight(props.height),
    margin: props.margin
  }">

    <n-el tag="div" class="box-left" />
    <n-el tag="div" class="box-right" />
    <n-el tag="div" class="box-right_top" />
    <n-el tag="div" class="box-left_down" />
    <n-el tag="div" class="box-content">
      <n-el tag="div">
        <slot>
          xy-box-1
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
  background-image: url("@/assets/hz-box/xy-1/bg.png");
  background-size: 100% 100%;
}

.box-left{
  position: absolute;
  top: 0;
  left: 0;
  width: 10px;
  height: 10px;
  background-image: url("@/assets/hz-box/xy-1/left_up.png");
  background-size: 100% 100%;
}
.box-right{
  position: absolute;
  bottom: 0;
  right: 0;
  width: 10px;
  height: 10px;
  background-image: url("@/assets/hz-box/xy-1/right_down.png");
  background-size: 100% 100%;
}

.box-right_top{
  position: absolute;
  top: 0;
  right: 0;
  width: 10px;
  height: 10px;
  background-image: url("@/assets/hz-box/xy-1/right_up.png");
  background-size: 100% 100%;
}

.box-left_down{
  position: absolute;
  bottom: 0;
  left: 0;
  width: 10px;
  height: 10px;
  background-image: url("@/assets/hz-box/xy-1/left_down.png");
  background-size: 100% 100%;
}
.box-content{
  position: absolute;
  top: 20px;
  left: 30px;
  width: calc(100% - 49px);
  height: calc(100% - 40px);


  // 第一个div
  > div:nth-child(1){
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 20px;
    font-size: 20px;
    font-weight: 600;
    color: #fff;
    line-height: 20px;
  }

  // 第二个div
  > div:nth-child(2){
    margin-top: 5px;
    position: absolute;
    top: 20px;
    left: 0;
    width: 100%;
    height: calc(100% - 25px);
  }

}
</style>