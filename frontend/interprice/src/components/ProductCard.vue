<template>
  <ion-card class="ion-text-center ion-align-items-stretch">
    <img @click="() => router.push({ name: 'ProductDetails', params: { supermarket: supermarket, productId: productId }})" :src=imageUrl height="150" width="150" />
    <ion-card-header class="ion-text-start" button router-link="{ name: 'ProductDetails', params: { supermarket: supermarket, productId: productId}}">
      <ion-card-subtitle>
        <ion-text>{{ supermarket }}</ion-text>
      </ion-card-subtitle>
      <ion-card-title>
        <ion-text>
          <h5>{{ name }}</h5>
        </ion-text>
      </ion-card-title>
    </ion-card-header>
    <ion-card-content class="ion-text-start">
      <ion-text><strong>{{ $filters.currency(price) }}</strong></ion-text>
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
  props: {
    productId: Number,
    supermarket: String,
    name: String,
    imageUrl: String,
    price: Number
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