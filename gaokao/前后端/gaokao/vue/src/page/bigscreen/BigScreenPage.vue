<template>
  <n-config-provider :theme="theme" class="hz-bg-one">
    <n-global-style />
    <hz-top-one width="100%" height="80px" title="高考可视化及预测" @click="toBack"/>
    <n-el tag="div" class="hz-main">
      <n-el class="middle1">

        <n-el class="up">
          <dv-border-box8 dur="8" style="width: 100%;height: 100%" >
            <n-el class="updemo">
              <n-button style="margin-top:5px;margin-left: 5px;width: 60px;height: 40px;background-color: rgba(11,118,232,0.68)" v-for="item in shengshi" :key="item" type="primary" @click="city_change(item)">{{item}}</n-button>
            </n-el>
            </dv-border-box8>
        </n-el>
        <dv-border-box8 dur="8" style="height: 80%;
  display: flex;
  justify-content: center;
  align-items: center;">
        <n-el class="down">
          <n-el class="down_neirong">
            <n-el class="card" v-for="(item,index) in schoolinfo" :key="index" @click="getinfoschool(item['schoolid'])">
              <n-el class="icon">
                <n-image :src="localImge(item['schoolid'])" object-fit="scale-down" style="width: 100%;height: 100%"></n-image>
              </n-el>
              <n-el class="name">
                <n-el class="schoolname">{{item['name']}}</n-el>
                <n-el class="schoolscore">
                  <n-el class="schollscoremiddle">
                    <n-el class="ininin">学校类型：{{item['school_types']}}</n-el>
                    <n-el class="ininin">学校批次：{{item['school_pici']}}</n-el>
                  </n-el>
                  <n-el class="schollscoremiddle">
                    <n-el class="ininin">学校类别：{{item['school_leibie']}}</n-el>
                    <n-el class="ininin">分数/名次：{{item['score']}}/{{item['weici']}}</n-el>
                  </n-el>
                </n-el>
              </n-el>
            </n-el>
          </n-el>

        </n-el>
        <n-pagination v-model:page="page" :page-count="max_page" @click="changepage(page)" style="  margin-left: 2%;
"/>
        </dv-border-box8>
      </n-el>
      <n-el class="middle2">
        <dv-border-box8 dur="8" style=" width: 100%;height: 50%;display: flex;justify-content: center;align-items: center;">
        <n-el class="in1" v-if="change_show">
          <n-el class="in_title">推荐学校</n-el>
          <n-el class="in_const">
         <n-el class="in_const_card">
           <n-el>语文</n-el>
           <n-input-number v-model:value="chinese_value" :show-button="false" max="150" min="0"/>
         </n-el>
            <n-el class="in_const_card">
              <n-el>英语</n-el>
              <n-input-number v-model:value="english_value" :show-button="false" max="150" min="0"/>
            </n-el>
            <n-el class="in_const_card">
              <n-el>数学</n-el>
              <n-input-number v-model:value="math_value" :show-button="false" max="150" min="0"/>
            </n-el>
            <n-el class="in_const_card">
              <n-el>综合</n-el>
              <n-input-number v-model:value="all_value" :show-button="false" max="300" min="0"/>
            </n-el>
          </n-el>
          <n-el class="yuce">
            <n-button @click="yuce_button" style="background-color: #006ce0">预测</n-button>
          </n-el>
          <n-el style="height: 90%">
            <n-el class="in_answer">{{ school_yuce }}</n-el>
            <n-el class="in_answer">录取概率高</n-el>
          </n-el>

        </n-el>
        <n-el class="in1" v-if="!change_show">
          <n-el class="in_title">被录取概率预测</n-el>
          <n-el class="in_answer" style="height: 40%" @click="change">{{ getyucezhi }}</n-el>
          <n-el class="in_const">
            <n-el class="in_const_card">
              <n-el>语文</n-el>
              <n-input-number v-model:value="chinese_value" :show-button="false" max="150" min="0"/>
            </n-el>
            <n-el class="in_const_card">
              <n-el>英语</n-el>
              <n-input-number v-model:value="english_value" :show-button="false" max="150" min="0"/>
            </n-el>
            <n-el class="in_const_card">
              <n-el>数学</n-el>
              <n-input-number v-model:value="math_value" :show-button="false" max="150" min="0"/>
            </n-el>
            <n-el class="in_const_card">
              <n-el>综合</n-el>
              <n-input-number v-model:value="all_value" :show-button="false" max="300" min="0"/>
            </n-el>

          </n-el>
          <n-el class="yuce">
            <n-button @click="yuce_button2">预测</n-button>
          </n-el>
        </n-el>
        </dv-border-box8>

        <dv-border-box8 dur="8" style=" width: 100%;height: 50%;display: flex;justify-content: center;align-items: center;">
        <n-el class="in1">
          <n-el class="in1_title">学校详情</n-el>
          <n-el class="in1_neirong">
            <n-el style="height: 20%;width: 96%;margin-left: 2%">
              学校名称：{{ schoolName}}
            </n-el>
            <n-el style="height: 60%;width: 96%;margin-left: 2%">
              学校详情：{{ jianjie }}
            </n-el>

            <n-el style="height: 20%;width: 96%;margin-left: 2%">
              其他详情：<a :href="schoolOther">点击查看</a>
            </n-el>
          </n-el>

        </n-el>
          </dv-border-box8>
      </n-el>
      <n-el class="middle2">
        <dv-border-box8 dur="8" style=" width: 100%;height: 50%;display: flex;justify-content: center;align-items: center;">
        <n-el class="in1">
          <Hz-Echarts-Bar-Simple ref="simpleBar" id="simpleBar"></Hz-Echarts-Bar-Simple>
        </n-el>
          </dv-border-box8>
        <dv-border-box8 dur="8" style=" width: 100%;height: 50%;display: flex;justify-content: center;align-items: center;">
        <n-el class="in1">
          <Hz-Echarts-Pie-Simple ref="simplePie" id="simplePie"></Hz-Echarts-Pie-Simple>
        </n-el>
          </dv-border-box8>
      </n-el>

    </n-el>

  </n-config-provider>
</template>

<script setup>

import {theme} from "@/bean/config";
import HzTopOne from "@/components/hz-top/one/Hz-Top-One.vue";
import router from "@/router";
import HzEchartsPieSimple from "@/components/echarts/pie/Hz-Echarts-Pie-Simple.vue";
import HzEchartsBarSimple from "@/components/echarts/bar/Hz-Echarts-Bar-Simple.vue";
import {onMounted, ref} from "vue";
import { BorderBox8 as DvBorderBox8 } from '@kjgl77/datav-vue3'
import {
  getPredictDataBySchool,
  getSchoolDateByAddress,
  getSchoolDateById,
  getSchoolDateBySubject
} from "@/api/gaokao/Schooldate-API";
import {getAllXunlianshujuForBar} from "@/api/gaokao/Xunlianshuju-API";
import {getAllScorecountForPie} from "@/api/gaokao/ScoreCount-API";
import {getSchoolinfoallById} from "@/api/gaokao/Schoolinfoall-API";
const page = ref(1)
const shengshi = ref(['北京', '上海', '重庆', '天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江',
  '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北',
  '湖南', '广东', '广西', '海南', '四川', '贵州', '云南', '西藏',
  '陕西', '甘肃', '青海', '宁夏', '新疆']);
const schoolinfo = ref([])
const chinese_value = ref(0)
const english_value = ref(0)
const math_value = ref(0)
const all_value = ref(0)
const schoolName = ref('xx大学')
const school_yuce = ref('xx大学')
const schoolAddress = ref('重庆市沙坪坝区')
const schoolType = ref('物理')
const schoolBatch = ref('本科批')
const schoolOther = ref('https://www.baidu.com')
const schoolscore = ref(300)
const getyucezhi = ref('预测学校录取概率')
const change_show = ref(true)
const max_page = ref(100)
const simpleBar = ref(null);
const simplePie = ref(null);
const nowCity = ref('北京')
const jianjie = ref('暂时没有数据,请点击学校查看详情')

function city_change(item){
  SchoolDateByAddress(item);
  nowCity.value = item
}

function getinfoschool(id){
  getSchoolByid(id)
  change_show.value = false
}
function getSchoolByid(id){
  getSchoolDateById({id:id}).then(res=>{
    schoolName.value = res.data.name
    schoolAddress.value = res.data.address
    schoolType.value = res.data.school_types
    schoolBatch.value = res.data.school_pici
    schoolscore.value = res.data.score
    //res.data.schoolid
    schoolOther.value = "https://www.gaokao.cn/school/"+res.data.schoolid
  })
  getSchoolinfoallById({id:id}).then(res=>{
    if (res.code!=200){
      console.log("没有数据")
    }
    else {
      jianjie.value = res.data.data[0].jainjie
    }
  })
}
function yuce_button2(){
  console.log("11111")

  console.log(schoolscore.value)
  getPredictDataBySchool({chinese:chinese_value.value,english:english_value.value,math:math_value.value,all:all_value.value,schoolscore:schoolscore.value}).then(res=>{
    console.log(res)
    if (res.data == 1){
      getyucezhi.value = "录取概率高"}
      else{
        getyucezhi.value = "录取概率低"
    }

  })
}
function changepage(page){
  SchoolDateByAddress(nowCity.value,page);
}
function change(){
  change_show.value = true
}
function yuce_button(){

  console.log(chinese_value.value)
  console.log(english_value.value)
  console.log(math_value.value)
  console.log(all_value.value)
  getSchoolDateBySubject({chinese:chinese_value.value,english:english_value.value,math:math_value.value,all:all_value.value}).then(res=>{
    console.log(res.data)
    school_yuce.value = res.data.name
    schoolName.value = res.data.name
    schoolAddress.value = res.data.address
    schoolType.value = res.data.school_types
    schoolBatch.value = res.data.school_pici
    //res.data.schoolid
    schoolOther.value = "https://www.gaokao.cn/school/"+res.data.schoolid

  })
}
function SchoolDateByAddress(address,page){
  getSchoolDateByAddress({address:address,page:page}).then(res=>{
    console.log(res.data.data)
    schoolinfo.value = res.data.data
    max_page.value = res.data.count
    console.log(schoolinfo.value)


  })
}
onMounted(()=>{
  SchoolDateByAddress('北京');
  //每3秒刷新一次
  let i = 1;
  setInterval(()=>{
    i++;
    lianshujuForBar(i)
  },3000)
})

AllScorecountForPie()

const toBack = () => {
  router.push({path: '/index'})
}

const localImge = (id) => {
  return require(`@/assets/img/${id}.jpg`);
}


function lianshujuForBar(page){
  if( simpleBar.value==null){
    return
  }
  getAllXunlianshujuForBar({page:page}).then(res=>{
    simpleBar.value.refreshCharts({
      title: '训练数据分数集',
      x: res.data.x,
      y: res.data.y
    })
})
}

function AllScorecountForPie(){
  getAllScorecountForPie().then(res=>{
    simplePie.value.refreshCharts({
      title: '训练分数占比',
      data: res.data
    })
  })
}
</script>

<style lang="less" scoped>
.hz-bg-one {
  background: url("@/assets/hz-bg/one.png") no-repeat;
  background-size: 100% 100%;
  position: relative;
  width: 100%;
  height: 100%;
}

.hz-main {
  width: 100%;
  height: calc(100% - 80px);
  //水平居中
  display: flex;
}
.middle1 {
  width: 40%;
  height: 100%;
}
.middle2{
  width: 30%;
  height: 100%;
}
.hz-row {
  width: 100%;
  height: 33%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}
.in1 {
  width: 98%;
  height: 98%;
  color: white;
}
.up {
  width: 100%;
  height: 20%;
  //水平垂直居中
  display: flex;
  justify-content: center;
  align-items: center;

}
.updemo{
  width: 100%;
  height: 96%;
  //弹性布局
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  //垂直居中
  align-items: center;
  //滚动条
  overflow-y: scroll;
  //隐藏滚动条
  &::-webkit-scrollbar {
    display: none;
  }
}
.down {
  width: 96%;
  height: 92%;
  //水平垂直居中
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 1%;
}
.in_title {
  width: 100%;
  height: 20%;
  //居中
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 25px;
  color: white;
  //加粗
  font-weight: bold;
}
.in_const {
  width: 98%;
  height: 30%;
  //居中
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(26, 37, 73, 0.53);
  margin-left: 2%;

}
.in_answer {
  width: 98%;
  height: 20%;
  //居中
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: rgba(73, 240, 253, 0.53);
  margin-left: 2%;

  color: white;
  font-size: 40px;
  //加粗
  font-weight: bold;
}
.in1_title {
  width: 100%;
  height: 25%;
  //居中
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 25px;
  color: white;
  //加粗
  font-weight: bold;
}
.in1_neirong {
  width: 100%;
  height: 75%;
  background-color: rgba(26, 37, 73, 0.53);

}
.down_neirong {
  width: 100%;
  height: 100%;
  //垂直弹性布局
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  flex-wrap: wrap;
  //垂直滚动条
  overflow-y: scroll;
  //隐藏滚动条
  scrollbar-width: none;
  &::-webkit-scrollbar {
    display: none;
  }

}
.card {
  width: 96%;
  height: 35%;
  margin-top: 1%;
  //水平布局
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-left: 2%;
}
.icon {
  width: 32%;
  height: 100%;
  //居中
  display: flex;
  justify-content: center;
  align-items: center;

}
.name {
  width: 64%;
  height: 100%;
  background-color: rgba(26, 37, 73, 0.53);
}
.in_const_card{
  width: 20%;
  height: 100%;
  //垂直居中
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-left: 3%;

}
.schoolname{
  width: 100%;
  height: 30%;
  //垂直居中
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  color: white;
  //加粗
  font-weight: bold;

}
.schoolscore{
  width: 100%;
  height: 60%;
  //垂直居中
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  font-size: 15px;
  color: white;
  margin-top: 3%;
  //加粗
  font-weight: bold;
  .schollscoremiddle{
    width: 49%;
    height: 100%;
    //垂直居中
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin-left: 1%;
    .ininin{
      width: 100%;
      height: 48%;
      background-color: rgb(24, 159, 217);
      //垂直居中
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      margin-top: 1%;
    }
  }
}
.yuce{
  width: 98%;

// 水平居右
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-end;
}
</style>