<!--
  具体的操作参考高德地图官方文档
  https://lbs.amap.com/api/javascript-api-v2/prerequisites
  根据自己的需求进行修改，案例代码仅供参考 init()方法中的代码
-->

<template>
  <div :id='props.id' ref="gaode_map"  class="main-box"></div>
  <div id="panel"></div>
</template>

<script setup>

import AMapLoader from '@amap/amap-jsapi-loader';
import {onMounted, ref, shallowRef} from "vue";
import {useMessage} from "naive-ui";
const message = useMessage();

window._AMapSecurityConfig = {
  securityJsCode: '1702a50ab3e02cf7dccbab0228ca0dc8', // 申请的安全码
}

// eslint-disable-next-line no-undef
const props = defineProps({
  id: {
    type: String,
    default: 'gaode_map'
  },
  // 是否显示实时路况图层
  isShowTraffic: {
    type: Boolean,
    default: false
  },
});

const map = shallowRef(null) //shallowRef() 与 ref() 的区别是 shallowRef() 是浅层的，它不会对内部的数据进行响应式转换，而 ref() 会对内部数据进行响应式转换

const pointMarker = ref([])

const placeSearch = shallowRef(null)
const driving = shallowRef(null)

function init() {
  AMapLoader.load({
    key: '5021342326e4eee35cf66bd532c2b08b', // 申请好的Web端开发者Key，首次调用 load 时必填
    version: '2.0', // 指定要加载的 JSAPI 的版本，缺省时默认为 1.4.15
    plugins:['AMap.Autocomplete', 'AMap.PlaceSearch', 'AMap.Scale', 'AMap.OverView', 'AMap.ToolBar', 'AMap.MapType', 'AMap.PolyEditor', 'AMap.CircleEditor','AMap.Driving','AMap.PlaceSearch']
  }).then((AMap) => {
    // 初始化地图
    map.value = new AMap.Map(props.id, {
      viewMode: '3D', // 是否为3D地图模式
      resizeEnable: true, //是否监控地图容器尺寸变化
      zoom: 5, //级别 数字越大越精细
      center: [116.397428, 39.90923]  //初始化地图中心点
    });
    // map.value.setStatus({
    //   zoomEnable:false, // 禁止缩放
    //   dragEnable: false, // 禁止滑动
    // })
    // TODO 实时路况图层
    if (props.isShowTraffic){
      // 添加实时路况图层
      const traffic = new AMap.TileLayer.Traffic({
        'autoRefresh': true,     //是否自动刷新，默认为false
        'interval': 180,         //刷新间隔，默认180s
      });
      map.value.add(traffic); //通过add方法添加图层
    }
    // TODO 点标记，默认样式为红色的圆点，如果需要自定义样式，可以通过content属性来自定义点标记覆盖物内容
    if ( pointMarker.value != null ){
      // 显示点标记
      for (let i = 0; i < pointMarker.value.length; i++) {
        const marker = new AMap.Marker(
            pointMarker.value[i]
        );
        map.value.add(marker);
      }
    }
    // TODO 搜索地点，搜索结果展示在指定的容器中，必须在地图加载完成后调用，否则会出现空指针异常
     placeSearch.value = new AMap.PlaceSearch({
      pageSize: 5, // 单页显示结果条数
      pageIndex: 1, // 页码
      map: map.value, // 展现结果的地图实例
      panel: "panel", // 结果列表将在此容器中进行展示。
      autoFitView: true // 是否自动调整地图视野使绘制的 Marker点都处于视口的可见范围
    });
    driving.value = new AMap.Driving({
      map: map.value,
    });
  }).catch(e => {
    console.log(e);
  });
}

onMounted(() => {
  init()
});

function addMarker(lng,lat,contentText) {
  // 向pointMarker数组中追加数据
  let point = {
    position: [lng, lat], // Marker经纬度
    content: '<div style="position: relative;background: rgba(255,0,0,0.5);width: 50px;height: 50px;' +
        'border-radius: 90%;display: flex;justify-content: center;align-items: center;' +
        'left: -25px;top: -25px;font: 12px">'+contentText+'</div>', // 自定义点标记覆盖物内容
  }
  pointMarker.value.push(point)
  init()
}

function clearMarker() {
  pointMarker.value = []
}

//搜索地点
function searchMap(keyword) {
   placeSearch.value.search(keyword)
}

//规则路线
function searchDriving(points) {
  console.log(points)
  driving.value.search(points, function(status, result) { // 使用地点名称
    if (status === 'complete') {
      console.log('绘制驾车路线完成')
    } else {
      if (result === 'USER_DAILY_QUERY_OVER_LIMIT') {
        message.error('已达到最大路线规划数目，请明天再试')
      }
    }
  });
}

function searchDriving_lnglat(start,end) {
  driving.value.search(start,end, function(status, result) { // 使用地点名称
    if (status === 'complete') {
      console.log('绘制驾车路线完成')
    } else {
      if (result === 'USER_DAILY_QUERY_OVER_LIMIT') {
        message.error('已达到最大路线规划数目，请明天再试')
      }else{
        message.error('路线规划失败'+result)
      }
    }
  });
}

// eslint-disable-next-line no-undef
defineExpose({
  addMarker,
  clearMarker,
  searchMap,
  searchDriving,
  searchDriving_lnglat
});

</script>

<style scoped>
.main-box{
  width: 100%;
  height: 100%;
  color: black;
}

#panel {
  position: absolute;
  background-color: white;
  max-height: 90%;
  overflow-y: auto;
  top: 10px;
  right: 10px;
  width: 280px;
}

</style>