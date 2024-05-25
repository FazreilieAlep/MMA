<template>
  <button :class="['darksoul-hover-fill-button1', { 'clicked-style': clicked }]" type="button">
    <div class="color-fill-1"></div>
    <p><slot></slot></p>
  </button>
</template>

<script setup>
const props = defineProps({
  clicked: Boolean
})
</script>

<style scoped>
.darksoul-hover-fill-button1 {
  margin: auto;
  display: flex;
  width: 100px;
  height: 100px;
  border-radius: 5px;
  outline: none;
  border: 1px solid #38a877;
  background-color: white;
  font-family: 'Belanosima', sans-serif;
  cursor: pointer;
  align-items: center;
  justify-content: left;
  position: relative;
  overflow: hidden; /* Ensure the color-fill-1 doesn't overflow the button */
}
.color-fill-1 {
  position: absolute;
  margin-left: -7px;
  width: 2px;
  height: 100px;
  background-color: #38a877;
  visibility: hidden;
  transition: all cubic-bezier(0.445, 0.05, 0.55, 0.95) 0.5s;
}
.darksoul-hover-fill-button1:hover .color-fill-1 {
  visibility: visible;
  width: 100px;
  height: 100px;
  border-radius: 5px;
}
.darksoul-hover-fill-button1:hover {
  box-shadow: 1px 1px 20px rgb(160, 216, 255);
  transition: all 1s;
}
.darksoul-hover-fill-button1 p {
  margin: auto;
  z-index: 10;
}

/* New style when clicked is true */
.clicked-style {
  background-color: #38a877;
  color: white;
  border: 1px solid white;
}

/* phone res */
@media only screen and (max-width: 1024px) and (min-height: 1920px) {
  .darksoul-hover-fill-button1 {
    width: 200px;
    height: 200px;
  }

  .color-fill-1 {
    position: absolute;
    margin-left: -7px;
    width: 2px;
    height: 200px;
    background-color: #38a877;
    visibility: hidden;
    transition: all cubic-bezier(0.445, 0.05, 0.55, 0.95) 0.5s;
  }
  .darksoul-hover-fill-button1:hover .color-fill-1 {
    visibility: visible;
    width: 200px;
    height: 200px;
    border-radius: 10px;
  }
}
</style>
