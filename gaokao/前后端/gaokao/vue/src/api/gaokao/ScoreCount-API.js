
import result from '@/util/axios.js'

export function list(query) {
  return result({
    url:'/hzapi/scorecount/getScorecount',
    method:'get',
    params:query
  })
}

export function update(query) {
  return result({
    url:'/hzapi/scorecount/updateScorecount',
    method:'post',
    data:query
  })
}

export function add(query) {
  return result({
    url:'/hzapi/scorecount/addScorecount',
    method:'post',
    data:query
  })
}

export function del(query) {
  return result({
    url:'/hzapi/scorecount/deleteScorecount',
    method:'delete',
    params:query
  })
}

export function getAllScorecountForPie(query) {
    return result({
        url:'/hzapi/scorecount/getAllScorecountForPie',
        method:'get',
        params:query
    })

}