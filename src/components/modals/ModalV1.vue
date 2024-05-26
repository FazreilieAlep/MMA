<template>
  <div v-if="isVisible" class="modal-overlay" @click="close">
    <div class="modal-content" @click.stop>
      <header class="modal-header">
        <slot name="header">
          <h3>Modal Header</h3>
        </slot>
        <Button
          @click="close"
          icon="pi pi-times"
          severity="danger"
          text
          rounded
          aria-label="Cancel"
        />
      </header>
      <main class="modal-body">
        <slot name="body">
          <p>This is the modal content</p>
        </slot>
      </main>
      <footer class="modal-footer">
        <slot name="footer">
          <Button @click="close" label="Close" severity="danger" text raised />
        </slot>
      </footer>
    </div>
  </div>
</template>

<script>
import Button from 'primevue/button'
export default {
  name: 'ModalV1',
  props: {
    visible: {
      type: Boolean,
      required: true
    },
    db: String
  },
  computed: {
    isVisible() {
      return this.visible
    }
  },
  methods: {
    close() {
      this.$emit('update:visible', false)
      this.$emit('closed')
    }
  }
}
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000;
}

.modal-content {
  background: white;
  padding: 1rem;
  border-radius: 8px;
  width: auto;
  max-width: 100%;
  box-shadow: 0 5px 15px hsla(0, 0%, 0%, 0.3);
  animation: fadeIn 0.3s;
  height: -webkit-fill-available;
  overflow: auto;
}

.modal-content::-webkit-scrollbar {
  width: 0;
}

.modal-header,
.modal-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  color: rgb(34, 34, 34);
}

.close-button {
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@media only screen and (max-width: 1024px) and (min-height: 1920px) {
}
</style>
