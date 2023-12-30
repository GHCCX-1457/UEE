import result from '@/util/axios.js'

export function registerAccount(query) {
  return result({
    url:'/hzapi/auth/register',
    method:'post',
    data:query,
      headers:{
          'Content-Type':'application/x-www-form-urlencoded',
          'Authorization':'test'
      }
  })
}

export function loginIn(query) {
  return result({
    url:'/hzapi/auth/login',
    method:'post',
    data:query,
    headers:{
        'Content-Type':'application/x-www-form-urlencoded',
        'Authorization':'test',

    },

  })
}

export function getUserInfo(query) {
    return result({
        url:'/hzapi/auth/getInfo',
        method:'get',
        params:query,
        headers:{
            'Content-Type':'application/x-www-form-urlencoded',
            //当前用户的token(登录后返回的token)
            'Authorization':localStorage.getItem('token')
        },
    })
}

export function setUserInfo(query) {
    return result({
        url:'/hzadmin/userinfo/',
        method:'post',
        data:query,
    })
}

export function logout(query) {
    // 删除token
    localStorage.removeItem('token')
  return result({
    url:'/hzadmin/logout',
    method:'get',
    params:query
  })
}
