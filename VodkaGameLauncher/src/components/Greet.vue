
<template>
  <div class="card flex justify-content-center">
      <Toast />
      <div class="flex flex-wrap gap-2">
          <Button label="Success" severity="success" @click="showSuccess" />
          <Button label="Info" severity="info" @click="showInfo" />
          <Button label="Warn" severity="warning" @click="showWarn" />
          <Button label="Error" severity="danger" @click="showError" />
      </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useToast } from "primevue/usetoast";
const toast = useToast();

const showSuccess = () => {
  toast.add({ severity: 'success', summary: 'Success Message', detail: 'Message Content', life: 3000 });
};

const showInfo = () => {
  toast.add({ severity: 'info', summary: 'Info Message', detail: 'Message Content', life: 3000 });
};

const showWarn = () => {
  toast.add({ severity: 'warn', summary: 'Warn Message', detail: 'Message Content', life: 3000 });
};

const showError = () => {
  toast.add({ severity: 'error', summary: 'Error Message', detail: 'Message Content', life: 3000 });
};

onMounted(() => {
  setTimeout(() => {
    showSuccess();
  }, 3000); // Delay for 3 seconds
});

</script>