<!-- 词云 -->
<template>
  <div :id="props.id" style="width: 100%; height: 100%;"></div>
</template>

<script setup>
import 'echarts-wordcloud';
import * as echarts from 'echarts';
import { defineProps, defineExpose } from 'vue';

const props = defineProps({
  title: {
    type: String,
    default: ''
  },
  id: {
    type: String,
    default: ''
  }
});

const option = {
  title: {
    text: props.title,
    left: 'center',
    textStyle: {
      color: '#fff'
    }
  },
  tooltip: {
    show: true
  },
  series: [
    {
      type: 'wordCloud',
      // shape这个属性虽然可配置，但是在词的数量不太多的时候，效果不明显，它会趋向于画一个椭圆
      shape: 'circle',
      // 这个功能还没用过
      keepAspect: false,
      // 这个是可以自定义背景图片的，词云会按照图片的形状排布，所以有形状限制的时候，最好用背景图来实现，而且，这个背景图一定要放base64的，不然词云画不出来
      // maskImage: maskImage,
      // 下面就是位置的配置
      left: 'center',
      top: 'center',
      width: '70%',
      height: '80%',
      right: null,
      bottom: null,
      // 词的大小，最小12px，最大60px，可以在这个范围调整词的大小
      sizeRange: [12, 60],
      // 每个词旋转的角度范围和旋转的步进
      rotationRange: [-90, 90],
      rotationStep: 45,
      // 词间距，数值越小，间距越小，这里间距太小的话，会出现大词把小词套住的情况，比如一个大的口字，中间会有比较大的空隙，这时候他会把一些很小的字放在口字里面，这样的话，鼠标就无法选中里面的那个小字，这里可以用函数根据词云的数量动态返回间距
      gridSize: 8,
      // 允许词太大的时候，超出画布的范围
      drawOutOfBound: false,
      // 布局的时候是否有动画
      layoutAnimation: true,
      // 这是全局的文字样式，相对应的还可以对每个词设置字体样式
      textStyle: {
        fontFamily: 'sans-serif',
        fontWeight: 'bold',
        // 颜色可以用一个函数来返回字符串，这里是随机色
        color: function () {
          // Random color
          return 'rgb(' + [
            Math.round(Math.random() * 160),
            Math.round(Math.random() * 160),
            Math.round(Math.random() * 160)
          ].join(',') + ')';
        }
      },
      emphasis: {
        focus: 'self',
        textStyle: {
          textShadowBlur: 10,
          textShadowColor: '#333'
        }
      },
      data: []
    }
  ]
};

// 刷新图表方式，该方法需要提供给外部调用
// eslint-disable-next-line no-unused-vars
const refreshCharts = (data) => {
  option.series[0].data = data;
  const basicBar = echarts.init(document.getElementById(props.id), 'dark');
  basicBar.setOption(option);
};

// eslint-disable-next-line no-undef
defineExpose({
  refreshCharts
});

</script>

<style scoped>

</style>