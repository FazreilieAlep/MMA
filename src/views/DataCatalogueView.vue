<script setup>
import { ref, onMounted } from 'vue'
import buttonV1 from '../components/buttons/buttonV1.vue'
import ListV1 from '../components/lists/listV1/ListV1.vue'
import http from '../http'

// Button state management
const buttons = ref([])

const selected_db = ref({
  path: '',
  name: '',
  acronym: ''
})
const datatable_list = ref([])

const handleButtonClick = (id) => {
  let anyButtonClicked = false

  buttons.value.forEach((button) => {
    if (button.id === id) {
      button.clicked = !button.clicked
      if (button.clicked) {
        selected_db.value = {
          name: button.text,
          path: button.path,
          acronym: button.button_text
        }
        anyButtonClicked = true // Set the flag if the button is clicked
        get_datatable_list(button.path)
      }
    } else {
      button.clicked = false
    }
  })

  if (!anyButtonClicked) {
    selected_db.value = { path: '', name: '', acronym: '' }
    datatable_list.value = []
  }
}

const get_datatable_list = (hostpath) => {
  http
    .get('/data/' + hostpath + '/json')
    .then((response) => {
      // Process response data
      if (Array.isArray(response.data)) {
        datatable_list.value = response.data.map((item, index) => ({
          id: index + 1, // Assign a unique ID starting from 1
          text: item.data,
          path: item.path,
          syncLoading: false
        }))
      }
    })
    .catch((error) => {
      console.error('There was an error!', error)
    })
  // console.log(hostpath)
}

// Fetch data from API on component mount
onMounted(() => {
  http
    .get('/data/json/')
    .then((response) => {
      // Process response data
      if (Array.isArray(response.data)) {
        buttons.value = response.data.map((item, index) => ({
          id: index + 1, // Assign a unique ID starting from 1
          button_text: item.acronyms,
          text: item.organization_name,
          path: item.path,
          clicked: false
        }))
      }
    })
    .catch((error) => {
      console.error('There was an error!', error)
    })
})
</script>

<template>
  <h1>Database</h1>
  <div class="button-container">
    <buttonV1
      v-for="button in buttons"
      :key="button.id"
      :clicked="button.clicked"
      @click="handleButtonClick(button.id)"
    >
      {{ button.button_text.toUpperCase() }}
    </buttonV1>
  </div>
  <div v-if="selected_db.name !== ''" class="data-list">
    <ListV1 :items_parent="selected_db" :items="datatable_list"></ListV1>
  </div>
  <div v-else><h3>Please select a database</h3></div>
</template>

<style>
.data-list {
  width: 100%;
}
.button-container {
  margin: 1em;
  display: flex;
  gap: 1em;
}

@media (min-width: 1024px) {
  .button-container {
    margin: 2em;
    display: flex;
    gap: 2em;
  }
}
</style>
