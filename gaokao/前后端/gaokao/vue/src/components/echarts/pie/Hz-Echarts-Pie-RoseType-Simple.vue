<!-- 饼图 -->
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
        title: '饼图',
        data:[
          { value: 40, name: 'Search Engine' },
          { value: 38, name: 'Direct' },
          { value: 32, name: 'Email' },
          { value: 30, name: 'Union Ads' },
          { value: 26, name: 'Video Ads' }
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
  tooltip: {
    trigger: 'item'
  },
  legend: {
    orient: 'vertical',
    left: 'left',
    textStyle: {
      color: "rgba(255, 255, 255, 1)"
    }
  },
  toolbox: {
    show: true,
    feature: {
      mark: { show: true },
      dataView: { show: true, readOnly: false },
      restore: { show: true },
      saveAsImage: { show: true }
    }
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: [50, 250],
      center: ['50%', '50%'],
      roseType: 'area',
      itemStyle: {
        borderRadius: 8
      },
      data: props.data.data,
      label: {
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
  option.series[0].data = data.data;
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