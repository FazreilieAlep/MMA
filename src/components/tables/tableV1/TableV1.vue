<template>
  <div class="card table-container">
    <DataTable
      v-if="!loading"
      :value="itemList"
      :filters="filters"
      :globalFilterFields="headers"
      tableStyle="min-width: 50rem;"
    >
      <!-- Custom header for global search and clear filter -->
      <template #header>
        <div class="flex justify-content-between">
          <div class="p-input-icon-left">
            <i class="pi pi-search" />
            <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
            <!-- Bound global filter value to search input -->
          </div>
        </div>
      </template>

      <!-- Dynamically generate columns -->
      <Column
        v-for="header in headers"
        :key="header"
        :field="header"
        :header="header"
        :sortable="true"
      />
    </DataTable>
    <div v-else class="loading"><i class="pi pi-spin pi-spinner" /></div>
    <!-- Loading indicator when data is being fetched -->
  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue'
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import InputText from 'primevue/inputtext'
import Button from 'primevue/button'
import 'primevue/resources/themes/saga-blue/theme.css' // theme
import 'primevue/resources/primevue.min.css' // core css
import 'primeicons/primeicons.css' // icons

const props = defineProps({
  itemList: {
    type: Array,
    required: true
  },
  loading: {
    type: Boolean,
    required: true
  }
})

const filters = ref({
  global: { value: null, matchMode: 'contains' }
})

// Compute headers dynamically based on the keys of the first item in itemList
const headers = computed(() => {
  if (props.itemList.length > 0) {
    return Object.keys(props.itemList[0])
  }
  return []
})

const clearFilter = () => {
  filters.value = {
    global: { value: null, matchMode: 'contains' }
  }
}
</script>

<style scoped>
.flex {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
}

.p-input-icon-left {
  position: relative;
  display: flex;
  align-items: center;
}

.p-input-icon-left i {
  position: absolute;
  left: 10px;
}

.p-input-icon-left input {
  padding-left: 2rem;
}

.p-datatable {
  margin-top: 1em !important;
}

.loading {
  height: 3em;
  text-align: center;
  padding: 1em;
  color: black;
}
</style>
