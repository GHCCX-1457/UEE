

import {createRouter,createWebHashHistory} from "vue-router"

const router = createRouter({   //createRouter   vue2中是 new Vue
    history : createWebHashHistory(),  //createWebHashHistory  ，v3文档 API里有 ，将模式修改 ，Vue2中是mode :history
    routes: [
        {
            name:'',
            path:'/',
            component:()=>import('../page/login/LoginPage.vue')
        },
        {
            name:'LoginPage',
            path:'/login',
            component:()=>import('../page/login/LoginPage.vue')
        },
        {
            name:'RegisterPage',
            path:'/register',
            component:()=>import('../page/register/RegisterPage.vue')
        },
        {
            name:'BigScreenPage',
            path:'/bigscreen',
            component:()=>import('../page/bigscreen/BigScreenPage.vue')
        },
        {
            name:'MainPage',
            path:'/main',
            component:()=>import('../page/index/MainPage.vue'),
            children:[
                {
                    name: 'IndexPage',
                    path: '/index',
                    component: () => import('@/page/index/index/IndexPage.vue')
                },
                {
                    name: 'UserInfoPage',
                    path: '/user/info',
                    component: () => import('@/page/index/user/UserInfoPage.vue')
                },
                
                {
                    name: 'CityCountPage',
                    path: '/gaokao/CityCount',
                    component: () => import('@/page/gaokao/CityCount-Page.vue')
                },
    
                {
                    name: 'PiciCountPage',
                    path: '/gaokao/PiciCount',
                    component: () => import('@/page/gaokao/PiciCount-Page.vue')
                },
    
                {
                    name: 'SchooldatePage',
                    path: '/gaokao/Schooldate',
                    component: () => import('@/page/gaokao/Schooldate-Page.vue')
                },
    
                {
                    name: 'ScoreCountPage',
                    path: '/gaokao/ScoreCount',
                    component: () => import('@/page/gaokao/ScoreCount-Page.vue')
                },
    
                {
                    name: 'XunlianshujuPage',
                    path: '/gaokao/Xunlianshuju',
                    component: () => import('@/page/gaokao/Xunlianshuju-Page.vue')
                },
    
            ]
        }
    ]
})

// 拦截白名单
const whiteList = ['/login', '/register']

// 登录拦截
router.beforeEach((to, from, next) => {
    if (whiteList.indexOf(to.path) !== -1) {
        next()
    } else {
        let token = localStorage.getItem('token')
        if (token === null || token === '' || token === undefined) {
            next('/login')
        } else {
            next()
        }
    }
})

export default router
    