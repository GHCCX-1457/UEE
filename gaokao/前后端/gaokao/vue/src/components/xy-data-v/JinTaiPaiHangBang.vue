<template>
  <div w50rem h25rem flex="~ col" justify-center items-center bg-dark>
    <div>
      <dv-capsule-chart :config="config" style="width:25rem;height:15rem" />
    </div>
  </div>
</template>
<script setup>

import {defineExpose, defineProps, reactive} from "vue";

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