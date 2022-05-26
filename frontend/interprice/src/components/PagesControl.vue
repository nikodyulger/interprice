<template>
  <ion-toolbar>
    <ion-button shape="round" slot="start" @click="previousPage">
      <ion-icon slot="icon-only" :icon="arrowBackOutline" />
    </ion-button>
    <ion-title>
      <ion-chip>
        <ion-label>Página</ion-label>
        <ion-select :value="store.currentPage" interface="action-sheet" @ionChange="changePage">
          <ion-select-option v-for="p in store.pages" :value="p" :key="p">{{ p }}</ion-select-option>
        </ion-select>
      </ion-chip>
    </ion-title>
    <ion-button shape="round" slot="end" @click="nextPage">
      <ion-icon slot="icon-only" :icon="arrowForwardOutline" />
    </ion-button>
  </ion-toolbar>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useCatalogStore } from "@/store/catalog";
import { arrowBackOutline, arrowForwardOutline } from "ionicons/icons";
import {
  IonButton,
  IonChip,
  IonToolbar,
  IonLabel,
  IonIcon,
  IonSelect,
  IonSelectOption,
} from "@ionic/vue";
export default defineComponent({
  name: "PagesControl",
  setup() {
    const store = useCatalogStore()
    return {
      store,
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
  },
  methods: {
    previousPage() {
      this.store.previousPage();
    },
    nextPage() {
      this.store.nextPage();
    },
    changePage(event: any) {
      this.store.changePage(event.detail.value);
    }
  },
});
</script>
<style scoped>
ion-title {
  text-align: center;
}
</style>
