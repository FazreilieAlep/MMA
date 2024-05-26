<script setup lang="ts">
import { RouterLink } from 'vue-router'
</script>

<template>
  <nav>
    <RouterLink to="/">Home</RouterLink> |
    <RouterLink to="/about">About</RouterLink>
  </nav>
</template>

<style scoped>
nav {
  margin: 1em;
}
@media only screen and (max-width: 1024px) and (min-height: 1920px) {
  nav {
    font-size: 3em;
  }
}
</style>
