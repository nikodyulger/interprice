<template>
  <ion-card>
    <img
      @click="() => router.push('/Carrefour/123')"
      src="https://static.carrefour.es/hd_350x_/img_pim_food/035834_00_1.jpg"
    />
    <ion-card-header button router-link="/Carrefour/123">
      <ion-card-subtitle>
        <ion-text>Carrefour</ion-text>
      </ion-card-subtitle>
      <ion-card-title>
        <ion-text>Banana a granel</ion-text>
      </ion-card-title>
    </ion-card-header>
    <ion-card-content>
      <ion-text><strong>1,25$</strong></ion-text>
    </ion-card-content>
    <ion-item lines="none">
      <ion-button size="small" slot="end">Comparar</ion-button>
    </ion-item>
  </ion-card>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import {
  IonItem,
  IonCard,
  IonCardHeader,
  IonCardContent,
  IonCardSubtitle,
} from "@ionic/vue";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "ProductCard",
  components: {
    IonItem,
    IonCard,
    IonCardHeader,
    IonCardContent,
    IonCardSubtitle,
  },
  setup() {
    const router = useRouter();
    return { router };
  },
});
</script>

<style scoped>
ion-card-content {
  font-size: 20px;
}
</style>