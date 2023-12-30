<!--基础折线图-->
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
  title: {
    text: props.data.title,
    left: 'center',
    textStyle: {
      color: '#fff'
    }
  },
  xAxis: {
    type: 'category',
    // data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    data: props.data.x,
    axisLabel:{
      color: '#fff'
    }
  },
  tooltip: {
    trigger: "axis",
    axisPointer: {
      type: "shadow"
    }
  },
  yAxis: {
    type: 'value',
    axisLabel:{
      color: '#fff'
    }
  },
  grid:{
    left: '0%',
    right: '0%',
    bottom: '0%',
    top: '10%',
    containLabel: true,
  },
  series: [
    {
      // data: [150, 230, 224, 218, 135, 147, 260],
      data: props.data.y,
      type: 'bar',
      showBackground: true,
      label: {
        show: true,
        position: 'top',
        color: '#fff'
      },
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
  option.title.text = data.title;
  option.xAxis.data = data.x;
  option.series[0].data = data.y;
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