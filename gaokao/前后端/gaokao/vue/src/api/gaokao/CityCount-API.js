
import result from '@/util/axios.js'

export function list(query) {
  return result({
    url:'hzapi/citycount/getCitycount',
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
    url:'hzapi/citycount/updateCitycount',
    method:'post',
    data:query
  })
}

export function add(query) {
  return result({
    url:'hzapi/citycount/addCitycount',
    method:'post',
    data:query,

  })
}

export function del(query) {
  return result({
    url:'hzapi/citycount/deleteCitycount',
    method:'delete',
    params:query
  })
}

    