<template>
  <ion-page>
    <ion-header :translucent="true">
      <ion-toolbar>
        <ion-title>Interprice</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content :fullscreen="true">
      <ion-header collapse="condense">
        <ion-toolbar>
          <ion-title size="large">Promociones</ion-title>
        </ion-toolbar>
      </ion-header>

      <ion-list>
        <PromoListItem v-for="promo in promos" :key="promo.id" :promo="promo" />
      </ion-list>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import axios from "axios";
import {
  IonContent,
  IonHeader,
  IonList,
  IonPage,
  IonTitle,
  IonToolbar,
} from "@ionic/vue";
import PromoListItem from "@/components/PromoListItem.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Home",
  data() {
    return {
      promos: null,
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/promos")
      .then((res) => (this.promos = res.data))
      .catch((err) => console.log(err.message));
  },
  components: {
    IonContent,
    IonHeader,
    IonList,
    IonPage,
    IonTitle,
    IonToolbar,
    PromoListItem,
  },
});
</script>