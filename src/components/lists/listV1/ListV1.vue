<script setup>
import { ref } from 'vue'
import Button from 'primevue/button'
import ModalV1 from '@/components/modals/ModalV1.vue'
import TableV1 from '@/components/tables/tableV1/TableV1.vue'
import http from '@/http'
import { useConfirm } from 'primevue/useconfirm'
import { useToast } from 'primevue/usetoast'

function capitalizeInitials(str) {
  return str
    .split(' ')
    .map((word) => {
      return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase()
    })
    .join(' ')
}

const toast = useToast()

const showModal = ref(false)
const selected_datatable = ref('')
const tableItem = ref([])
const loading = ref(false)

const props = defineProps({
  items_parent: Object,
  items: Array
})

const get_datatable = (path) => {
  loading.value = true
  http
    .get('/data/' + props.items_parent.path + '/' + path + '/json')
    .then((response) => {
      if (Array.isArray(response.data)) {
        tableItem.value = response.data
      }
      loading.value = false
    })
    .catch((error) => {
      console.error('There was an error!', error)
      loading.value = false
    })
}

const handleModalButtonClick = (path = '', text = '') => {
  if (!showModal.value) {
    selected_datatable.value = text
    get_datatable(path)
    showModal.value = true
  } else {
    showModal.value = false
    selected_datatable.value = ''
    tableItem.value = [] // Reset tableItem when modal is closed
  }
}

const handleSyncButtonClick = (item = {}) => {
  item.syncLoading = true
  const fetchData = http.get('/data/' + props.items_parent.path + '/' + item.path + '/update-db')
  const delay = new Promise((resolve) => setTimeout(resolve, 1000)) // Minimum delay of 1 second

  Promise.all([fetchData, delay])
    .then(([response]) => {
      console.log(response.data)
      item.syncLoading = false
      setTimeout(() => {
        item.syncLoading = false
        toast.add({
          severity: 'info',
          summary: 'Synchronized',
          detail:
            capitalizeInitials(item.text) +
            ' from ' +
            props.items_parent.acronym.toUpperCase() +
            ' ' +
            response.data,
          life: 3000
        })
      }, 1000) // 1 second delay
    })
    .catch((error) => {
      console.error('There was an error!', error)
      item.syncLoading = false
      toast.add({
        severity: 'error',
        summary: 'Error',
        detail: 'Synchronization failed',
        life: 3000
      })
    })
}

const handleModalClosed = () => {
  selected_datatable.value = ''
  tableItem.value = []
}
</script>

<template>
  <section class="list-container">
    <!-- Header Bar -->
    <header>
      <div class="datatable-col">
        <label>DataTable</label>
      </div>

      <div class="action-col">
        <label>Action</label>
      </div>
    </header>

    <div class="list-item-container" v-if="props.items.length > 0">
      <ul class="items">
        <!-- List Item -->
        <li v-for="item in props.items" :key="item.id" class="item">
          <div class="datatable">
            <div style="padding-left: 0.5em">
              <h4 @click="handleModalButtonClick(item.path, item.text)">
                {{ capitalizeInitials(item.text) }}
              </h4>
            </div>
          </div>

          <div class="action">
            <Button icon="pi pi-pencil" severity="secondary" text raised rounded />
            <Button
              @click="handleSyncButtonClick(item)"
              v-tooltip="'Sync data'"
              :icon="item.syncLoading ? 'pi pi-spin pi-spinner' : 'pi pi-sync'"
              severity="Success"
              text
              raised
              rounded
            />
          </div>
        </li>
      </ul>
    </div>
    <div v-else class="items" style="display: flex; justify-content: center; margin: 1em">
      <h4>No data</h4>
    </div>
  </section>
  <Toast />
  <ModalV1 v-model:visible="showModal" @closed="handleModalClosed">
    <template #header>
      <h3>
        {{ items_parent.acronym.toUpperCase() }} | {{ capitalizeInitials(selected_datatable) }}
      </h3>
    </template>
    <template #body>
      <TableV1 :itemList="tableItem" :loading="loading" />
    </template>
    <template #footer>
      <Button @click="handleModalButtonClick()" label="Close" severity="danger" text raised />
    </template>
  </ModalV1>
</template>

<style scoped>
ModalV1 {
  overflow: hidden;
}
.datatable-col {
  width: 70%;
}

.action-col,
.action {
  width: 30%;
  display: flex;
  justify-content: center;
}

.list-container {
  margin: 0 auto;
  width: 70%;
  overflow: auto;
}

.list-container::-webkit-scrollbar {
  width: 0px;
}

header {
  padding: 0.5em;
  background-color: #888787;
  color: #252529;
  display: flex;
  align-items: center;
  font-size: 1em;
  font-weight: 600;
  box-sizing: border-box;
  user-select: none;
  text-align: left;
  border-radius: 5px;

  .datatable-col {
    margin-left: 1em;
  }
}

ul {
  padding: 0;
  li {
    display: flex;
    align-items: center;
    border-radius: 5px;
    padding: 0.3em;
    margin-top: 0.3em;

    div.datatable {
      width: 70%;
      padding: 0.5em;
      margin-left: 1em;
    }

    div.action {
      width: 30%;
      gap: 1em;
    }
  }

  li:hover {
    background-color: rgb(240, 248, 255, 0.1);
  }
}

h4:hover {
  list-style-type: none;
  cursor: pointer;
  color: aquamarine;
}

.list-item-container {
  overflow: auto;
  max-height: 190px;
}

.list-item-container::-webkit-scrollbar {
  display: none !important;
  width: 0px;
}

@media only screen and (max-width: 1024px) and (min-height: 1920px) {
  .list-container {
    margin: 0 auto;
    width: 100%;
    overflow: auto;
  }

  .list-item-container {
    max-height: 500px;
  }
}
</style>
