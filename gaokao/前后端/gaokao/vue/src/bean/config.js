import {ref} from "vue";
import {darkTheme} from 'naive-ui'
export const theme = ref(localStorage.getItem('theme') === 'dark' ? darkTheme : null);
export const isDark = ref(localStorage.getItem('theme') === 'dark'? true : false);

export const switchTheme = (value) => {
    theme.value = value ? darkTheme : null;
    // 写入本地存储
    localStorage.setItem('theme', value ? 'dark' : 'light');
}