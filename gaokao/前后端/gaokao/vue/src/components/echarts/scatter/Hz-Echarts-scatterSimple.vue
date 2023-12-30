<!--基础散点图-->
<template>
  <div :id="props.id" class="main-box"></div>
</template>

<script setup>
import * as echarts from 'echarts';
import {onMounted} from "vue";

// eslint-disable-next-line no-undef
const props = defineProps({
  id: {
    type: String,
    default: ''
  },
  data: {
    type: Array,
    default: () => {
      return []
    }
  },
  theme: {
    type: String,
    default: '' // 'dark'
  }
});

const option = {
  //铺满整个div
  grid: {
    left: '0%',
    right: '5%',
    bottom: '0%',
    top: '10%',
    containLabel: true
  },

  xAxis: {

  },

  yAxis: {

  },
  series: [
    {
      // data: [150, 230, 224, 218, 135, 147, 260],]

      data: props.data.data,
      type: 'scatter',
      symbolSize: 5,
    }
  ]
};

onMounted(() => {
  init()
});

function init() {
  const basicBar = echarts.init(document.getElementById(props.id), props.theme);
  basicBar.setOption(option);
}

// 刷新图表方式，该方法需要提供给外部调用
// eslint-disable-next-line no-unused-vars
const refreshCharts = (data) => {
  option.series[0].data = data.data;
  init();
};

// eslint-disable-next-line no-undef
defineExpose({
  refreshCharts
});

</script>

<style scoped>
.main-box {
  width: 100%;
  height: 100%;
}
</style>