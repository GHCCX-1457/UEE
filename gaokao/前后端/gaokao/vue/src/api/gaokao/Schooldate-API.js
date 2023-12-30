
import result from '@/util/axios.js'

export function list(query) {
  return result({
    url:'/hzapi/schooldate/getSchooldate',
    method:'get',
    params:query
  })
}

export function update(query) {
  return result({
    url:'/hzapi/schooldate/updateSchooldate',
    method:'post',
    data:query
  })
}

export function add(query) {
  return result({
    url:'/hzapi/schooldate/addSchooldate',
    method:'post',
    data:query
  })
}

export function del(query) {
  return result({
    url:'/hzapi/schooldate/deleteSchooldate',
    method:'delete',
    params:query
  })
}

export function getSchoolDateByAddress(query) {
    return result({
        url:'/hzapi/schooldate/getSchooldateByAddress',
        method:'get',
        params:query
    })
}

//根据学科预测大学
export function getSchoolDateBySubject(query) {
    return result({
        url:'/hzapi/schooldate/getPredictData',
        method:'post',
        data:query
    })
}

//根据id查询大学
export function getSchoolDateById(query) {
    return result({
        url:'/hzapi/schooldate/getSchooldateById',
        method:'get',
        params:query
    })
}

//根据分数预测录取概率
export function getPredictDataBySchool(query) {
    return result({
        url:'/hzapi/schooldate/getPredictDataBySchool',
        method:'post',
        data:query
    })
}