<!--K线图-->
<template>
  <div :id="props.id" style="width: 100%;height: 100%"></div>
</template>

<script setup>
import * as echarts from 'echarts';
import {onMounted} from "vue";

// eslint-disable-next-line no-undef
const props = defineProps({
  title: {
    type: String,
    default: ''
  },
  id: {
    type: String,
    default: ''
  },
  theme: {
    type: String,
    default: 'dark' // 'dark'
  },
  data: {
    type: Array,
    default: () => {
      return {
        time: ['2017-10-24', '2017-10-25', '2017-10-26', '2017-10-27'],
        data: [
          [20, 34, 10, 38],
          [40, 35, 30, 50],
          [31, 38, 33, 44],
          [38, 15, 5, 42]
        ]
      }
    }
  }
});

const option = {
  backgroundColor: "rgba(0,0,0,0)",
  title: {
    text: '基础K线图',
    left: 0,
    textStyle: {
      color: '#fff'
    }
  },
  xAxis: {
    data: props.data.time,
  },
  yAxis: {},
  series: [
    {
      type: 'candlestick',
      data: props.data.data,
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
const refreshCharts = (title,time,data) => {
  option.title.text = title;
  option.xAxis.data = time;
  option.series[0].data = data;
  const basicBar = echarts.init(document.getElementById(props.id),props.theme);
  basicBar.clear();
  basicBar.setOption(option);
};

// eslint-disable-next-line no-undef
defineExpose({
  refreshCharts
});
</script>

<style scoped>

</style>