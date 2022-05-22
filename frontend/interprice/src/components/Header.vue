<template>
  <ion-header class="ion-no-border">
    <ion-toolbar color="tertiary">
      <ion-title slot="start">
        <ion-text @click="() => router.push('/')">Interprice</ion-text>
      </ion-title>
    </ion-toolbar>
  </ion-header>
</template>

<script lang="ts">
import { IonHeader, IonToolbar, IonText } from "@ionic/vue";
import { defineComponent } from "vue";
import { useRouter } from "vue-router";

export default defineComponent({
  components: {
    IonHeader,
    IonToolbar,
    IonText,
  },
  data() {
    return {
      search: "",
    };
  },
  setup() {
    const router = useRouter();
    return { router };
  },
});
</script>

<style scoped>
</style>