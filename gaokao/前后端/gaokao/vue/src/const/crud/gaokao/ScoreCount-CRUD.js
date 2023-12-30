import {ref} from "vue";

export const _itemInfo = ref([

    {label: 'score', key: 'score',disabled: false,show: true},
    {label: 'count', key: 'count',disabled: false,show: true},
    {label: 'id', key: 'id',disabled: true,show: true},
])
    
export const itemInfo = ref({

        score: '',
        count: '',
        id: '',
})
    
export const pagination = ref({
    page: 1,
    pageSize: 10,
    pageCount: 100,
})
    
export const columnsOption = ref([
    
    {title: 'score', key: 'score',width:100,ellipsis: {tooltip: true}},
    {title: 'count', key: 'count',width:100,ellipsis: {tooltip: true}},
    {title: 'id', key: 'id',width:100,ellipsis: {tooltip: true}},
])
    