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
        title: '动态排序',
        label: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        data: [150, 230, 224, 218, 135, 147, 260]
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
    max: 'dataMax'
  },
  yAxis: {
    type: 'category',
    data: props.data.label,
    inverse: true,
    animationDuration: 300,
    animationDurationUpdate: 300,
    max: 7 // only the largest 3 bars will be displayed
  },
  legend: {
    orient: 'vertical',
    left: 'left',
    textStyle: {
      color: "rgba(255, 255, 255, 1)"
    }
  },
  animationDuration: 0,
  animationDurationUpdate: 1000,
  animationEasing: 'linear',
  animationEasingUpdate: 'linear',
  series: [
    {
      realtimeSort: true,
      name: 'Access From',
      type: 'bar',
      data: getRandomData(),
      label: {
        show: true,
        position: 'right',
        valueAnimation: true,
        color: "rgba(255, 255, 255, 1)"
      },
    }
  ]
};

onMounted(() => {
  init()
  interval=setInterval(()=>{
      run()
      init()
    },1000)
});

let data = []
let interval = null

function getRandomData(){
  let datas = []
  for (var i=0;i<props.data.data.length;i++){
    datas.push(0)
  }
  return datas
}

function run(){
  let max_num = 0
  for(var i=0;i<props.data.data.length;i++){
    if(data[i] == null){
      data[i] = 0
    }if(data[i]>=props.data.data[i]){
      data[i] = props.data.data[i]
      max_num += 1
    }else{
      data[i] = data[i] + Math.random() * 100
    }
  }
  option.series[0].data = data
  if (max_num == props.data.data.length){
    clearInterval(interval)
  }
}


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
  interval=setInterval(()=>{
    run()
    init()
  },1000)
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