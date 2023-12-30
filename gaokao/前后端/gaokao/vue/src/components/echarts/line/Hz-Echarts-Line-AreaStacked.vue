<!-- 堆叠面积图 -->
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
        title: '堆叠面积图',
        x: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        name: ['邮件营销', '联盟广告', '视频广告', '直接访问', '搜索引擎'],
        y: [
          [120, 132, 101, 134, 90, 230, 210],
          [220, 182, 191, 234, 290, 330, 310],
          [150, 230, 224, 218, 135, 147, 260],
          [320, 332, 301, 334, 390, 330, 320],
          [820, 932, 901, 934, 1290, 1330, 1320],
        ]
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
  xAxis: {
    type: 'category',
    data: props.data.x,
  },
  yAxis: {
    type: 'value'
  },
  tooltip: {
    trigger: 'axis'
  },
  legend: {
    orient: 'vertical',
    left: 'left',
    textStyle: {
      color: "rgba(255, 255, 255, 1)"
    }
  },
  series: getSeries(props.data.name,props.data.y)
};

// 分割props.data.y 为多个series
function getSeries(name,y) {
  let series = [];
  for (let i = 0; i < y.length; i++) {
    series.push({
      name: name[i],
      type: 'line',
      stack: 'Total',
      areaStyle: {},
      data: y[i],
      containLabel: true,
      label: {
        show: true,
        color: "rgba(255, 255, 255, 1)"
      },
    })
  }
  return series;
}

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
  option.series = getSeries(data.name,data.y);
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