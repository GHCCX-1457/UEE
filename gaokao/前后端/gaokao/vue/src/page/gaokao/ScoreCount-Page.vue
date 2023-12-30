
<template>
  <n-space item-style="margin-top:10px;margin-left:50px">
    <n-button type="primary" @click="addView">新增</n-button>
  </n-space>
  <n-space justify="center" item-style="width: 100%;margin-top:10px;">
    <n-data-table
        :columns="columns"
        :data="data"
        :loading="loading"
        striped
    />

  </n-space>
  <n-space justify="center" item-style="width: 100%;margin-top:10px;">
    <n-pagination
        v-model:page="pagination.page"
        v-model:pageSize="pagination.pageSize"
        :pageCount="pagination.pageCount"
        :showSizePicker="pagination.showSizePicker"
        :pageSizes="pagination.pageSizes"
        @update-page="loadList"
        @update-page-size="loadList"
    />
  </n-space>
  <n-modal
      v-model:show="showModal"
      class="custom-card"
      preset="card"
      :title="addOrUpdate ? '新增' : '编辑'"
      size="huge"
      :bordered="false"
      :segmented="segmented"
  >
    <n-form
        label-placement="top"
        :model="itemInfo"
    >
      <n-form-item v-for="item in _itemInfo" :key="item" :label="item.label" v-show="item.show==true">
        <n-input v-model:value="itemInfo[item.key]" :disabled="item.disabled"/>
      </n-form-item>
    </n-form>
    <template #footer>
      <n-space>
        <n-button type="primary" @click="addItemInfo" v-show="addOrUpdate">添加</n-button>
        <n-button type="primary" @click="updateItemInfo" v-show="!addOrUpdate">保存</n-button>
        <n-button type="primary" @click="showModal = false">取消</n-button>
      </n-space>
    </template>
  </n-modal>
</template>

<script setup>

import {h, onMounted, ref} from "vue";
import {NButton, NPopconfirm, useMessage} from "naive-ui";
import {add, del, list, update} from "@/api/gaokao/ScoreCount-API";
import {_itemInfo, columnsOption, itemInfo, pagination} from "@/const/crud/gaokao/ScoreCount-CRUD";

const message = useMessage();

const columns = ref([
  {
    title: '操作',
    key: 'action',
    fixed: 'right',
    width: 200,
    render: (row) => {
      return [
        h(NButton, {type: 'primary', ghost: true,onClick: () => editView(row),style:'margin-left:10px'}, '编辑'),
        h(
            NPopconfirm,
            {
              positiveButtonProps: {
                bordered: true,
              },
              negativeButtonProps: {
                bordered: true,
              },
              positiveText: '确认',
              negativeText: '取消',
              onPositiveClick: () => delView(row),
            },
            {
              trigger: () => {
                return h(
                    NButton,
                    {
                      type: 'error',
                      ghost: true,
                      style:'margin-left:10px'
                    },
                    { default: () => '删除' }
                )
              },
              default: () => {
                return '确认删除该节点？'
              }
            }
        )
      ]
    },
  },
])

const addOrUpdate = ref(false)

const loading = ref(false)

const data = ref([])

const showModal = ref(false)

const segmented = ref({
  content: true,
  footer: 'soft'
})

onMounted(() => {
  columns.value = columnsOption.value.concat(columns.value)
  loadList()
})


function loadList() {
  loading.value = true
  list(
      {
        page: pagination.value.page,
        size: pagination.value.pageSize
      }
  ).then(res => {
    data.value = res.data.data
    pagination.value.pageCount = res.data.count
    loading.value = false
  })
}

function addView() {
  addOrUpdate.value = true
  showModal.value = true
  for (let key in itemInfo.value) {
    itemInfo.value[key] = ''
  }
}

function editView(row) {
  console.log('edit',row)
  showModal.value = true
  itemInfo.value = row
}

function delView(row) {
  console.log('del',row)
  del({
    id: row.id
  }).then(res => {
    if (res.code !== 200) {
      message.error(res.msg)
      return
    }
    message.success('删除成功')
    loadList()
  })
}

function updateItemInfo() {
  update(itemInfo.value).then(res => {
    if (res.code !== 200) {
      message.error(res.msg)
      return
    }
    console.log(res)
    message.success('保存成功')
    showModal.value = false
    loadList()
  })
}

function addItemInfo() {
  // 删掉id
  add(itemInfo.value).then(res => {
    if (res.code !== 200) {
      message.error(res.msg)
      return
    }
    message.success('添加成功')
    showModal.value = false
    loadList()
  })
}

</script>

<style lang="less" scoped>

</style>
    