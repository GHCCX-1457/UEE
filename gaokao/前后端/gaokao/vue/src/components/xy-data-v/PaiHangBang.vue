<template>
  <div w50rem h24rem p3 flex="~ col" justify-center items-center bg-dark>
    <div>
      <dv-scroll-ranking-board :config="config" style="width:400px;height:240px" />

    </div>

  </div>
</template>
<script setup>

import {reactive,defineProps,defineExpose} from "vue";
const props = defineProps({
  title: {
    type: String,
    default: ''
  },
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
  unit: {
    type: String,
    default: () => {
      return ''
    }
  }
});
const config = reactive({
  // carousel: 'page',//翻页类型
  textColor: 'rgba(5,127,245,0.83)',
  color:  'rgba(90,201,201,0.66)',

  data: props.data,
  unit: props.unit,

})

const refreshPaiHang=(data)=>{
  config.data=data.data
  config.unit=data.unit
}
defineExpose({
  refreshPaiHang
});
</script>

<!--{name: '公司1', value: 100},
      {name: '公司2', value: 200},
      {name: '公司3', value: 300},
      {name: '公司4', value: 400},
      {name: '公司5', value: 500},
      {name: '公司6', value: 600},
      {name: '公司7', value: 700},
      {name: '公司8', value: 800},
      {name: '公司9', value: 900},
      {name: '公司10', value: 1000},-->