import result from '@/util/axios.js'

export function getSchoolinfoallById(query) {
    return result({
        url:'/hzapi/schoolinfoall/getSchoolinfoallById',
        method:'get',
        params:query
    })
    }
