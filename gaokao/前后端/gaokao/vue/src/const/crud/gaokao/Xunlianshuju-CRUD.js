import {ref} from "vue";

export const _itemInfo = ref([

    {label: 'like_school', key: 'like_school',disabled: false,show: true},
    {label: 'wenke_school', key: 'wenke_school',disabled: false,show: true},
    {label: 'chinese', key: 'chinese',disabled: false,show: true},
    {label: 'math', key: 'math',disabled: false,show: true},
    {label: 'english', key: 'english',disabled: false,show: true},
    {label: 'physics', key: 'physics',disabled: false,show: true},
    {label: 'chemistry', key: 'chemistry',disabled: false,show: true},
    {label: 'biology', key: 'biology',disabled: false,show: true},
    {label: 'politics', key: 'politics',disabled: false,show: true},
    {label: 'history', key: 'history',disabled: false,show: true},
    {label: 'geography', key: 'geography',disabled: false,show: true},
    {label: 'location', key: 'location',disabled: false,show: true},
    {label: 'time', key: 'time',disabled: false,show: true},
    {label: 'wenke_score', key: 'wenke_score',disabled: false,show: true},
    {label: 'like_score', key: 'like_score',disabled: false,show: true},
    {label: 'id', key: 'id',disabled: true,show: true},
])
    
export const itemInfo = ref({

        like_school: '',
        wenke_school: '',
        chinese: '',
        math: '',
        english: '',
        physics: '',
        chemistry: '',
        biology: '',
        politics: '',
        history: '',
        geography: '',
        location: '',
        time: '',
        wenke_score: '',
        like_score: '',
        id: '',
})
    
export const pagination = ref({
    page: 1,
    pageSize: 10,
    pageCount: 100,
})
    
export const columnsOption = ref([
    
    {title: 'like_school', key: 'like_school',width:100,ellipsis: {tooltip: true}},
    {title: 'wenke_school', key: 'wenke_school',width:100,ellipsis: {tooltip: true}},
    {title: 'chinese', key: 'chinese',width:100,ellipsis: {tooltip: true}},
    {title: 'math', key: 'math',width:100,ellipsis: {tooltip: true}},
    {title: 'english', key: 'english',width:100,ellipsis: {tooltip: true}},
    {title: 'physics', key: 'physics',width:100,ellipsis: {tooltip: true}},
    {title: 'chemistry', key: 'chemistry',width:100,ellipsis: {tooltip: true}},
    {title: 'biology', key: 'biology',width:100,ellipsis: {tooltip: true}},
    {title: 'politics', key: 'politics',width:100,ellipsis: {tooltip: true}},
    {title: 'history', key: 'history',width:100,ellipsis: {tooltip: true}},
    {title: 'geography', key: 'geography',width:100,ellipsis: {tooltip: true}},
    {title: 'location', key: 'location',width:100,ellipsis: {tooltip: true}},
    {title: 'time', key: 'time',width:100,ellipsis: {tooltip: true}},
    {title: 'wenke_score', key: 'wenke_score',width:100,ellipsis: {tooltip: true}},
    {title: 'like_score', key: 'like_score',width:100,ellipsis: {tooltip: true}},
    {title: 'id', key: 'id',width:100,ellipsis: {tooltip: true}},
])
    