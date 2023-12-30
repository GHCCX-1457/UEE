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
  radar: {
    // shape: 'circle',
    indicator: props.data,
    name:{
      textStyle:{
        color:'#fff'
      }
    }
  },
  title: {
    left: 'center',
    textStyle: {
      color: '#fff'
    }
  },
  legend: {
    data: props.data,
    textStyle:{
      color:"#fff"
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
      data: props.data,
      type: 'radar',
      showBackground: true,
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
  option.legend.data = data.legend;
  option.radar.indicator = data.indicator;
  init();
  /**
   * title：String
   * data：Array
   * legend：Array
   * indicator：Array
   * */
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