const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
    //设置代理服务器
    devServer: {
        host: "0.0.0.0", //代表当前域名和ipv4域名下都行
        allowedHosts: 'all',//解决 Invalid Host header
        port: 8081,
        proxy: {
            '/': {
                target: 'http://127.0.0.1:5000/',
                changeOrigin: true, // 允许跨域
                withCredentials: true, // 允许携带cookie
                ws: false,
                pathRewrite: {
                    '^/': '/'
                }
            }
        }
    }
})
