import {ref} from "vue";

export const _itemInfo = ref([

    {label: 'schoolid', key: 'schoolid',disabled: false,show: true},
    {label: 'name', key: 'name',disabled: false,show: true},
    {label: 'address', key: 'address',disabled: false,show: true},
    {label: 'info', key: 'info',disabled: false,show: true},
    {label: 'img', key: 'img',disabled: false,show: true},
    {label: 'score', key: 'score',disabled: false,show: true},
    {label: 'weici', key: 'weici',disabled: false,show: true},
    {label: 'school_types', key: 'school_types',disabled: false,show: true},
    {label: 'school_pici', key: 'school_pici',disabled: false,show: true},
    {label: 'school_leibie', key: 'school_leibie',disabled: false,show: true},
    {label: 'id', key: 'id',disabled: true,show: true},
])
    
export const itemInfo = ref({

        schoolid: '',
        name: '',
        address: '',
        info: '',
        img: '',
        score: '',
        weici: '',
        school_types: '',
        school_pici: '',
        school_leibie: '',
        id: '',
})
    
export const pagination = ref({
    page: 1,
    pageSize: 10,
    pageCount: 100,
})
    
export const columnsOption = ref([
    
    {title: 'schoolid', key: 'schoolid',width:100,ellipsis: {tooltip: true}},
    {title: 'name', key: 'name',width:100,ellipsis: {tooltip: true}},
    {title: 'address', key: 'address',width:100,ellipsis: {tooltip: true}},
    {title: 'info', key: 'info',width:100,ellipsis: {tooltip: true}},
    {title: 'img', key: 'img',width:100,ellipsis: {tooltip: true}},
    {title: 'score', key: 'score',width:100,ellipsis: {tooltip: true}},
    {title: 'weici', key: 'weici',width:100,ellipsis: {tooltip: true}},
    {title: 'school_types', key: 'school_types',width:100,ellipsis: {tooltip: true}},
    {title: 'school_pici', key: 'school_pici',width:100,ellipsis: {tooltip: true}},
    {title: 'school_leibie', key: 'school_leibie',width:100,ellipsis: {tooltip: true}},
    {title: 'id', key: 'id',width:100,ellipsis: {tooltip: true}},
])
    