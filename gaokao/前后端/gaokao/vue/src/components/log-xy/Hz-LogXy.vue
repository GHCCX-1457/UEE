<template>
  <n-space vertical>

    <n-log ref="logInst" :log="log" language="naive-log" trim font-size=18 style="color: #76e8d0" rows="12"/>
  </n-space>
</template>

<script>
import { defineComponent, ref, watchEffect, onMounted, nextTick } from "vue";
/*
* 本周天气预报：晴转多云，气温20-25℃。
气象局发布暴雨蓝色预警，请注意防范。
受到冷空气影响，未来三天全国大部将出现降温。
今年第X次雾霾天气来临，注意减少户外活动。
台风“珊瑚”即将来袭，沿海地区做好准备。
北方多地出现沙尘暴，请大家注意防护。
南方地区遭遇强降雨，需注意交通安全。
高温天气持续，多地气温突破历史极值。
东北地区将迎来一轮较强降雪，需注意防寒保暖。
气象局发布雷电黄色预警，请尽量避免外出。
寒潮蓝色预警发布，请大家注意添衣保暖。
未来三天江南地区将持续阴雨天气。
华北黄淮等地将出现严重雾霾，注意健康防护。
四川盆地遭遇强暴雨袭击，需防范次生灾害。
新疆西部和南部将有较强降雪，需注意交通安全。
*
* */
//生成数组
const logArr = [
  "本周天气预报：晴转多云，气温20-25℃。",
  "气象局发布暴雨蓝色预警，请注意防范。",
  "受到冷空气影响，未来三天全国大部将出现降温。",
  "今年第十次雾霾天气来临，注意减少户外活动。",
  "台风“珊瑚”即将来袭，沿海地区做好准备。",
  "北方多地出现沙尘暴，请大家注意防护。",
  "南方地区遭遇强降雨，需注意交通安全。",
  "高温天气持续，多地气温突破历史极值。",
  "东北地区将迎来一轮较强降雪，需注意防寒保暖。",
  "气象局发布雷电黄色预警，请尽量避免外出。",
  "寒潮蓝色预警发布，请大家注意添衣保暖。",
  "未来三天江南地区将持续阴雨天气。",
  "华北黄淮等地将出现严重雾霾，注意健康防护。",
  "四川盆地遭遇强暴雨袭击，需防范次生灾害。",
  "新疆西部和南部将有较强降雪，需注意交通安全。",
    "大雪封山，注意交通安全。"
];
function log() {
  const l = [];
  for (let i = 0; i < 30; ++i) {
    //生成1-15的随机数
    const r = Math.floor(Math.random() * 15 + 1);


    l.push("[资讯] "+"".repeat(r) + logArr[r],);

  }
  return l.join("\n") + "\n";
}

export default defineComponent({
  setup() {
    const logRef = ref(log());
    const logInstRef = ref(null);
    const startRef = ref(true);
    const timerRef = ref(null);

    onMounted(() => {
      watchEffect(() => {
        if (logRef.value) {
          nextTick(() => {
            startRef.value = !startRef.value;
            if (startRef.value) {
              timerRef.value = window.setInterval(() => {
                logRef.value = logRef.value + log();
              }, 2e3);
            } else if (timerRef.value) {
              clearInterval(timerRef.value);
              timerRef.value = null;
            }
            logInstRef.value?.scrollTo({ position: "bottom", slient: true });
          });
        }
      });
    });
    //每隔1秒钟运行一次
    setInterval(() => {
      for(let i=0;i<logArr.length;i++){
        logRef.value = logRef.value + log();      }

    }, 2e3);

    return {
      log: logRef,
      logInst: logInstRef,

    };
  }
});
</script>