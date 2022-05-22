<template>
  <ion-toolbar>
    <ion-button shape="round" slot="start" @click="previousPage">
      <ion-icon slot="icon-only" :icon="arrowBackOutline" />
    </ion-button>
    <ion-title>
      <ion-chip>
        <ion-label>Página</ion-label>
        <ion-select value="1" interface="action-sheet">
          <ion-select-option>1</ion-select-option>
          <ion-select-option>2</ion-select-option>
          <ion-select-option>3</ion-select-option>
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
    return {
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
      alert("previousPage");
    },
    nextPage() {
      alert("nextPage");
    },
  },
});
</script>
<style scoped>
ion-title {
  text-align: center;
}
</style>
