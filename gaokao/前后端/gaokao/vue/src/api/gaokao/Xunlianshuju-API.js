
import result from '@/util/axios.js'

export function list(query) {
  return result({
    url:'/hzapi/xunlianshuju/getXunlianshuju',
    method:'get',
    params:query
  })
}

export function update(query) {
  return result({
    url:'/hzapi/xunlianshuju/updateXunlianshuju',
    method:'post',
    data:query
  })
}

export function add(query) {
  return result({
    url:'/hzapi/xunlianshuju/addXunlianshuju',
    method:'post',
    data:query
  })
}

export function del(query) {
  return result({
    url:'/hzapi/xunlianshuju/deleteXunlianshuju',
    method:'delete',
    params:query
  })
}

export function getAllXunlianshujuForBar(query) {
    return result({
        url:'/hzapi/xunlianshuju/getAllXunlianshujuForBar',
        method:'get',
        params:query
    })

}

    