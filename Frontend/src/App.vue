<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavBar from './components/NavBar.vue'
import Footer from './components/Footer.vue'
</script>

<template>
  <div class="main-container">
    <img
      alt="MMA logo"
      class="logo"
      src="@/assets/logo/malaysian-macroeconomic-analysis-high-resolution-logo-transparent.png"
    />
    <NavBar />
    <RouterView />
  </div>
  <Footer />
</template>

<style scoped>
.main-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 2em;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
  width: 400px;
  height: auto;
}

@media (min-width: 1024px) {
  .logo {
    margin: 2em;
    width: 600px;
    height: auto;
  }
}

/* phone res */
@media only screen and (max-width: 1024px) and (min-height: 1920px) {
  .main-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 2em;
    width: 100%;
  }
  .logo {
    display: block;
    margin: 2em;
    width: 100%;
    height: auto;
  }
}
</style>
