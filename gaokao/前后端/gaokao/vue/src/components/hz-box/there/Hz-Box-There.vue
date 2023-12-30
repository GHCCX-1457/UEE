<template>
  <n-el tag="div" class="box-main" :style="{
    width: getWidth(props.width),
    height: getHeight(props.height),
    margin: props.margin
  }">

    <n-el tag="div" class="box-right-one">
    </n-el>
    <n-el tag="div" class="box-top-two">
    </n-el>
    <n-el tag="div" class="box-left-one">
    </n-el>
    <n-el tag="div" class="box-right-top-two">
    </n-el>
    <n-el tag="div" class="box-left-bottom">
    </n-el>
    <n-el tag="div" class="box-bottom">
    </n-el>
    <n-el tag="div" class="box-right-bottom">
    </n-el>
    <n-el tag="div" class="box-content">
      <n-el tag="div">
        <slot name="title" />
      </n-el>
    </n-el>
    <n-el tag="div" class="box-content_two">

    </n-el>
    <n-el tag="div" class="box-content_tu">
      <slot name="content" />
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
  width: 5px;
  height: 100%;
}

.box-right-one{
  position: absolute;
  top: 60px;
  bottom: 20px;
  right: 0;
  width: 1.5px;
  background: #054251;
}

.box-left-one{
  position: absolute;
  top: 20px;
  bottom: 20px;
  left: 0;
  width: 1.5px;
  background: #054251;
}

.box-top-two{
  position: absolute;
  top: 0;
  left: 15px;
  width: 100%;
  height: 2px;
  background: #054251;
}

.box-bottom{
  position: absolute;
  bottom: 4px;
  left: 15px;
  width: 100%;
  height: 1.5px;
  background: #054251;
}


.box-right-top-two {
  position: absolute;
  top: 0;
  right: 0;
  width: 57px;
  height: 74px;
  background-image: url("@/assets/hz-box/there/biao2.png");
}
.box-left-bottom{
  position: absolute;
  bottom: 4px;
  left: 0;
  width: 19px;
  height: 19px;
  background-image: url("@/assets/hz-box/there/left_down.png");
}

.box-right-bottom{
  position: absolute;
  bottom: 4px;
  right: 0;
  width: 19px;
  height: 19px;
  background-image: url("@/assets/hz-box/there/rigth_down.png");
}

.box-content_two {
  position: absolute;
  top: 0;
  left: 57px;
  width: 500px;
  height: 74px;
  background-image: url("@/assets/hz-box/there/biao1.png");
}
.box-content{
  position: absolute;
  top: 0;
  left: 0;
  width: 60px;
  height: 74px;
  background-image: url("@/assets/hz-box/there/biao.png");

  // 第一个div
  > div:nth-child(1){
    position: absolute;
    top: 20px;
    left: 50px;
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
.box-content_tu {
  width: calc(100% - 20px);
  height: calc(100% - 20px);
  position: relative;
  margin: 10px;
  top: 60px;
}
</style>