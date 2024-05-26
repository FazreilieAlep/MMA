<template>
  <router-link :to="to" class="nav-button">
    <slot></slot>
  </router-link>
</template>

<script setup>
const props = defineProps({
  to: {
    type: String,
    required: true
  }
})
</script>

<style scoped>
.nav-button {
  display: inline-block;
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}
.nav-button:hover {
  background-color: #38a877;
}
</style>
