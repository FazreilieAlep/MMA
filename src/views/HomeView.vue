<script setup lang="ts">
import NavButton from '../components/NavButton.vue'
</script>

<template>
  <h1>Thorough Diagnosis of MY Market</h1>
  <h3>Discover more on Malaysia's Economics</h3>
  <div class="button-container">
    <div class="nav-button">
      <NavButton to="/data-catalogue">Data Catalogue</NavButton>
    </div>
    <div class="nav-button">
      <NavButton to="/analysis">Analysis Result</NavButton>
    </div>
  </div>
</template>

<style scoped>
.button-container {
  margin: 2em;
  display: flex;
  gap: 1em;
}
</style>
