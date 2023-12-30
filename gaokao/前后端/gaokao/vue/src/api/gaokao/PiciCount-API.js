
import result from '@/util/axios.js'

export function list(query) {
  return result({
    url:'hzapi/picicount/getPicicount',
    method:'get',
    params:query,
    headers:{
      'Content-Type':'application/x-www-form-urlencoded',
      //当前用户的token(登录后返回的token)
      'Authorization':localStorage.getItem('token')
    },
  })
}

export function update(query) {
  return result({
    url:'hzapi/picicount/updatePicicount',
    method:'post',
    data:query
  })
}

export function add(query) {
  return result({
    url:'hzapi/picicount/addPicicount',
    method:'post',
    data:query
  })
}

export function del(query) {
  return result({
    url:'hzapi/picicount/deletePicicount',
    method:'delete',
    params:query
  })
}

    