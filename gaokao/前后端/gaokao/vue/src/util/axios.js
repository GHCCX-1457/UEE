import axios from "axios";

//跨域请求，允许保存cookie
axios.defaults.withCredentials = true;

//返回其他状态码
axios.defaults.validateStatus = function (status) {
    return status >= 200 && status <= 500; //默认的
}

export const getCookie = name => {
    var strcookie = document.cookie// 获取cookie字符串
    var arrcookie = strcookie.split('; ')// 分割
    // 遍历匹配
    for (var i = 0; i < arrcookie.length; i++) {
        var arr = arrcookie[i].split('=')
        if (arr[0] === name) {
            return arr[1]
        }
    }
    return ''
}

//Http request 拦截器
axios.interceptors.request.use(
    config => {
        // 如果是Post请求则进行序列化
        if(config.method  === 'post' || config.method  === 'put'){
            config.headers['Content-Type'] = 'application/x-www-form-urlencoded';
        }
        return config;
    },error => {
        return Promise.reject(error);
    }
);

//Http response 拦截器
axios.interceptors.response.use(
    response => {
        const status = Number(response.status) || 200;
        if(status === 403){
            if(response.data.detail.indexOf("CSRF Failed: Origin checking failed") !== -1){
                return {
                    code: 403,
                    msg: 'CSRF验证失败'
                };
            }
        }
        if(status === 404){
            return {
                code: 404,
                msg: '请求资源不存在'
            }
        }
        if(status === 500){
            return {
                code: 500,
                msg: '服务器错误'
            }
        }
        if(status !== 200){
            return {
                code: status,
                msg: response.statusText
            }
        }
        if(status === 200){
            return {
                code: response.data.code,
                data: response.data.data,
                msg: response.data.msg
            }
        }
        return response;
    }
);

//表单序列化
export const serialize = data => {
    const list = [];
    Object.keys(data).forEach(ele => {
        list.push(`${ele}=${data[ele]}`);
    });
    return list.join("&");
};

export default axios;