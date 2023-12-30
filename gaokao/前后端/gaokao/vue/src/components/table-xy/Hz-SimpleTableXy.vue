<template>
  <n-data-table :columns="columns" :data="data"  />
</template>

<script setup>
import { defineProps } from 'vue'
// eslint-disable-next-line no-unused-vars
  const props = defineProps({
  columns: {
    type: Array,
    required: true,
    defineProps: () => {
      return []
    }
  },
  data: {
    type: Array,
    required: true,
    defineProps: () => {
      return []
    }
  }})
// eslint-disable-next-line vue/no-setup-props-destructure
const columns= props.columns;
// eslint-disable-next-line vue/no-setup-props-destructure
const data= props.data;


</script>