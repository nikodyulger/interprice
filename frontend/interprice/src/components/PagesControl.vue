<template>
  <ion-toolbar>
    <ion-button shape="round" slot="start" @click="catalog.previousPage" :disabled="catalog.currentPage === 1">
      <ion-icon slot="icon-only" :icon="arrowBackOutline" />
    </ion-button>
    <ion-title>
      <ion-chip>
        <ion-label>Página</ion-label>
        <ion-select :value="catalog.currentPage" :selectedText="catalog.currentPage" interface="action-sheet"
          @ionChange="catalog.changePage(Number($event.detail.value))">
          <ion-select-option v-for="p in catalog.pages" :key="p" :value="p">{{ p }}</ion-select-option>
        </ion-select>
      </ion-chip>
    </ion-title>
    <ion-button shape="round" slot="end" @click="catalog.nextPage" :disabled="catalog.currentPage === catalog.pages">
      <ion-icon slot="icon-only" :icon="arrowForwardOutline" />
    </ion-button>
  </ion-toolbar>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useCatalogStore } from "@/store/catalog";

import {
  IonButton,
  IonChip,
  IonToolbar,
  IonLabel,
  IonIcon,
  IonSelect,
  IonSelectOption,
  IonTitle
} from "@ionic/vue";

import { arrowBackOutline, arrowForwardOutline } from "ionicons/icons";
export default defineComponent({
  name: "PagesControl",
  setup() {
    const catalog = useCatalogStore()
    return {
      catalog,
      arrowBackOutline,
      arrowForwardOutline,
    };
  },
  components: {
    IonButton,
    IonChip,
    IonToolbar,
    IonLabel,
    IonIcon,
    IonSelect,
    IonSelectOption,
    IonTitle
  }
});
</script>
<style scoped>
ion-title {
  text-align: center;
}
</style>
