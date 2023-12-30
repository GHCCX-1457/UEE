<template>
  <n-el tag="div" :style="{width: getWidth(),height: getHeight()}" :class="props.openAnime ? 'anime-start' : 'anmie-none'">
  </n-el>
  <n-el tag="div" class="content">
    <n-el tag="div" class="title">
      <solt name="title">
        hz-anime-1 title
      </solt>
    </n-el>
    <n-el tag="div" class="desc">
      <solt name="desc">
        hz-anime-1 desc
      </solt>
    </n-el>
  </n-el>
</template>

<script setup>

// eslint-disable-next-line no-undef
const props = defineProps({
  openAnime: {
    type: Boolean,
    default: true
  },
});

function getWidth() {
  return `80px`
}

function getHeight() {
  return `111px`
}


</script>

<style scoped lang="less">

.anmie-none{
  width: 100%;
  height: 100%;
  animation: none;
  background: url("@/assets/hz-anime/dianchi/dianchi-0.png");
  background-size: 100% 100%;
}

.anime-start{
  width: 100%;
  height: 100%;
  background: url("@/assets/hz-anime/dianchi/dianchi-0.png");
  background-size: 100% 100%;
  position: relative;
  animation: dianchi 10s infinite;
}

@keyframes dianchi {
  0% {
    background: url("@/assets/hz-anime/dianchi/dianchi-0.png");
    background-size: 100% 100%;
  }
  5.8% {
    background: url("@/assets/hz-anime/dianchi/dianchi-1.png");
    background-size: 100% 100%;
  }
  11.6% {
    background: url("@/assets/hz-anime/dianchi/dianchi-2.png");
    background-size: 100% 100%;
  }
  17.4% {
    background: url("@/assets/hz-anime/dianchi/dianchi-3.png");
    background-size: 100% 100%;
  }
  23.2% {
    background: url("@/assets/hz-anime/dianchi/dianchi-4.png");
    background-size: 100% 100%;
  }
  29% {
    background: url("@/assets/hz-anime/dianchi/dianchi-5.png");
    background-size: 100% 100%;
  }
  34.8% {
    background: url("@/assets/hz-anime/dianchi/dianchi-6.png");
    background-size: 100% 100%;
  }
  40.6% {
    background: url("@/assets/hz-anime/dianchi/dianchi-7.png");
    background-size: 100% 100%;
  }
  46.4% {
    background: url("@/assets/hz-anime/dianchi/dianchi-8.png");
    background-size: 100% 100%;
  }
  52.2% {
    background: url("@/assets/hz-anime/dianchi/dianchi-9.png");
    background-size: 100% 100%;
  }
  58% {
    background: url("@/assets/hz-anime/dianchi/dianchi-10.png");
    background-size: 100% 100%;
  }
  63.8% {
    background: url("@/assets/hz-anime/dianchi/dianchi-11.png");
    background-size: 100% 100%;
  }
  69.6% {
    background: url("@/assets/hz-anime/dianchi/dianchi-12.png");
    background-size: 100% 100%;
  }
  75.4% {
    background: url("@/assets/hz-anime/dianchi/dianchi-13.png");
    background-size: 100% 100%;
  }
  81.2% {
    background: url("@/assets/hz-anime/dianchi/dianchi-14.png");
    background-size: 100% 100%;
  }
  87% {
    background: url("@/assets/hz-anime/dianchi/dianchi-15.png");
    background-size: 100% 100%;
  }
  92.8% {
    background: url("@/assets/hz-anime/dianchi/dianchi-16.png");
    background-size: 100% 100%;
  }
}

.content{
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;

  .title{
    font-size: 24px;
    color: #fff;
    text-align: center;
  }

  .desc{
    font-size: 16px;
    color: #fff;
    text-align: center;
  }
}

</style>