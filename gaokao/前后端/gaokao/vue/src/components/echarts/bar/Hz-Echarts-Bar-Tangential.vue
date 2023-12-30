<!-- 基础折线图 -->
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
    default: 'pie-simple'
  },
  data: {
    type: Array,
    default: () => {
      return {
        title: '极坐标',
        label: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        data: [150, 230, 224, 218, 135, 147, 260],
        max:300
      }
    }
  },
  theme: {
    type: String,
    default: 'dark' // 'dark'
  }
});

const option = {
  backgroundColor: "rgba(0,0,0,0)",
  title: {
    text: props.data.title,
    left: 'center',
    textStyle: {
      color: '#ffffff'
    }
  },
  polar: {
    radius: [30, '80%']
  },
  angleAxis: {
    max: props.data.max,
    startAngle: 75
  },
  radiusAxis: {
    type: 'category',
    data: props.data.label
  },
  tooltip: {},
  series: [
    {
      name: 'Access From',
      type: 'bar',
      data: props.data.data,
      coordinateSystem: 'polar',
      label: {
        show: true,
        position: 'middle',
        formatter: '{b}: {c}',
        color: "rgba(255, 255, 255, 1)"
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
  init()
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