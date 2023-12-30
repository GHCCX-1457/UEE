<template>
  <n-space vertical style="width: 88px; background-color: coral" >
    <n-select v-if="option.data!=null" v-model:value="value" :options="option.data" @update:value="handleUpdateValue" :id="props.id" style="background-color: fuchsia"/>
  </n-space>
</template>

<script setup>
import {ref, defineProps, defineEmits,} from "vue";
import {NSelect} from "naive-ui";
// import {onMounted} from "vue";
 import {findAllCityImg} from "@/api/anjuke/Anjuke-API";
const value=ref(null)
const emit = defineEmits(['child-event'])
const handleUpdateValue=(value,option)=>{
  console.log('emit'+emit)
  console.log(option.value)

  findAllCityImg({cnum:option.value}).then((res)=>{
    console.log("Mydounnnnnn"+res.code)
    emit('child-event',res.data)
  })

}

const props = defineProps({
  id: {
    type: String,
    default: ''

  },
  data: {
    type: Array,
    default: () => {
      return [
        {
          label: '1',
          value: '1'
        }

      ]
    },
    required: true
  }
});

const option = {
  data: props.data

}



const refresDropDown = (data) => {
  console.log(data)
  option.data = data.data;
  console.log("options"+option.data[0])
};

// eslint-disable-next-line no-undef
defineExpose({
  refresDropDown
});


</script>