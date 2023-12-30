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
          { value: 1048, name: 'Search Engine' },
          { value: 735, name: 'Direct' },
          { value: 580, name: 'Email' },
          { value: 484, name: 'Union Ads' },
          { value: 300, name: 'Video Ads' }
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
      radius: ['40%', '70%'],
      data: props.data.data,
      left: '0%',
      right: '0%',
      bottom: '0%',
      top: '0%',
      containLabel: true,
      itemStyle: {
        borderRadius: 10,
        borderColor: '#fff',
        borderWidth: 2
      },
      label: {
        color: "rgba(255, 255, 255, 1)",
        show: false,
        position: 'center'
      },
      emphasis: {
        label: {
          show: true,
          fontSize: 40,
          fontWeight: 'bold'
        }
      },
      labelLine: {
        show: false
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