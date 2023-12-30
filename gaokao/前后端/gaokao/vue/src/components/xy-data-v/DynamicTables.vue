<template>
  <div demo-bg>
    <dv-scroll-board :config="config" style="width:560px;height:280px" />
  </div>
</template>
<script setup>
import {reactive,defineProps,defineExpose} from "vue";
const props = defineProps({
  title: {
    type: Array,
    default: () => {
      return []
    }
  },
  id: {
    type: String,
    default: ''
  },
  data: {
    type: Array,
    default: () => {
      return [
        ['阿里巴巴', 'BABA', '1000'],
        ['腾讯', 'TCEHY', '2000'],
        ['百度', 'BIDU', '3000'],
        ['京东', 'JD', '4000'],
        ['美团', 'MEIT', '5000'],
        ['拼多多', 'PDD', '6000'],
        ['字节跳动', 'TCEHY', '7000'],
        ['小米', 'XIAOMI', '8000'],
        ['华为', 'HUAWEI', '9000'],
        ['网易', 'NTES', '10000'],
        ['携程', 'CTRP', '11000'],
        ['微博', 'WB', '12000'],
        ['搜狐', 'SOHU', '13000'],
        ['新浪', 'SINA', '14000'],
        ['滴滴', 'DIDI', '15000'],
        ['快手', 'KS', '16000'],
        ['美团', 'MEIT', '17000'],
        ['拼多多', 'PDD', '18000'],
        ['字节跳动', 'TCEHY', '19000'],
        ['小米', 'XIAOMI', '20000'],
        ['华为', 'HUAWEI', '21000'],
        ['网易', 'NTES', '22000'],
        ['携程', 'CTRP', '23000'],
        ['微博', 'WB', '24000'],
        ['搜狐', 'SOHU', '25000'],
        ['新浪', 'SINA', '26000'],
        ['滴滴', 'DIDI', '27000'],
        ['快手', 'KS', '28000'],
        ['美团', 'MEIT', '29000'],
        ['拼多多', 'PDD', '30000'],
        ['字节跳动', 'TCEHY', '31000'],
        ['小米', 'XIAOMI', '32000']]

    }
  },
})
const config = reactive({
  header: props.title,
  data:props.data,
  index: true,
  columnWidth: [50],
  align: ['center'],
  // eslint-disable-next-line no-undef
  headerBGC: 'rgba(28,129,239,0.78)',
  oddRowBGC: "rgba(5,238,215,0.78)",
  evenRowBGC: "rgba(5,238,215,0.53)",


})
const refreshDynamicTable=(data)=>{
  config.header=data.header
  config.data=data.data
  console.log("dynamicxxxxxxxx"+data.data)
}
defineExpose({
  refreshDynamicTable
});

</script>

<!--header: ['公司名称', '公司代码', '公司成交量'],
        data: [
          ['阿里巴巴', 'BABA', '1000'],
          ['腾讯', 'TCEHY', '2000'],
          ['百度', 'BIDU', '3000'],
          ['京东', 'JD', '4000'],
          ['美团', 'MEIT', '5000'],
          ['拼多多', 'PDD', '6000'],
          ['字节跳动', 'TCEHY', '7000'],
          ['小米', 'XIAOMI', '8000'],
          ['华为', 'HUAWEI', '9000'],
          ['网易', 'NTES', '10000'],
          ['携程', 'CTRP', '11000'],
          ['微博', 'WB', '12000'],
          ['搜狐', 'SOHU', '13000'],
          ['新浪', 'SINA', '14000'],
          ['滴滴', 'DIDI', '15000'],
          ['快手', 'KS', '16000'],
          ['美团', 'MEIT', '17000'],
          ['拼多多', 'PDD', '18000'],
          ['字节跳动', 'TCEHY', '19000'],
          ['小米', 'XIAOMI', '20000'],
          ['华为', 'HUAWEI', '21000'],
          ['网易', 'NTES', '22000'],
          ['携程', 'CTRP', '23000'],
          ['微博', 'WB', '24000'],
          ['搜狐', 'SOHU', '25000'],
          ['新浪', 'SINA', '26000'],
          ['滴滴', 'DIDI', '27000'],
          ['快手', 'KS', '28000'],
          ['美团', 'MEIT', '29000'],
          ['拼多多', 'PDD', '30000'],
          ['字节跳动', 'TCEHY', '31000'],
          ['小米', 'XIAOMI', '32000']]
      })-->