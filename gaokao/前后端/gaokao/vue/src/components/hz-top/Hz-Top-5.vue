<template>
  <n-el tag="div" class="hz_header" :style="{
    width:  props.width,
    height: props.height
  }">
    <span>
      <slot>
        hz-top-5
      </slot>
    </span>
  </n-el>
</template>

<script setup>

// eslint-disable-next-line no-undef
const props = defineProps({
  width: {
    type: String,
    default: '100%'
  },
  height: {
    type: String,
    default: '100%'
  },
});

</script>

<style scoped lang="less">
.hz_header{
  background: url("@/assets/hz-top/5/title.png") no-repeat;
  background-size: 100% 100%;
  position: relative;
  font-size: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.hz_header span{
  color: #fff;
  font-size: calc(60px * 0.60);
}
</style>