<template>
  <n-el tag="div" class="hz_header" :style="{
    width:  props.width,
    height: props.height
  }"
        :class="props.titleIndex === 1 ? 'title1' : 'title2'"
  >
    <span>
      <slot>
        hz-top-4
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
  titleIndex: {
    type: Number,
    default: 1
  }
});

</script>

<style scoped lang="less">
.hz_header{
  background: url("@/assets/hz-top/4/title1.png") no-repeat;
  font-size: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.title1{
  background: url("@/assets/hz-top/4/title1.png") no-repeat;
  background-size: 100% 100%;
}

.title2{
  background: url("@/assets/hz-top/4/title2.png") no-repeat;
  background-size: 100% 100%;
}

.hz_header span{
  color: #fff;
  font-size: calc(60px * 0.60);
}
</style>