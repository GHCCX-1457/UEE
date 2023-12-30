import { createApp } from 'vue'

import App from './App.vue'
import router from "./router/index.js"
import axios from "axios";
import naive from 'naive-ui'
import DataVVue3 from '@kjgl77/datav-vue3'

const app = createApp(App)

app.config.globalProperties.$axios = axios
app.use(naive)
app.use(DataVVue3)
app.use(router)
app.mount('#app')

