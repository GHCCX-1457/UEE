<template>
  <div w800px h320px flex="~ col" justify-center items-center bg-dark>
    <div>
      <dv-conical-column-chart :config="config" style="width:400px;height:200px;" />
    </div>
  </div>
</template>
<script  setup>


import {reactive,defineProps,defineExpose} from "vue";
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
})

const config = reactive({
  data: props.data,
  showValue: true,
  textColor: 'rgba(255,255,255,1)',
  columnColor: 'rgba(227,44,44,0.77)',
  color:[

  ]
})



const refreshZCharts=(data)=>{
  console.log("zuixing"+data.data)
  config.data=data.data
}
defineExpose({
  refreshZCharts
});
</script>