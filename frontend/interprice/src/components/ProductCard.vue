<template>
  <ion-card class="ion-text-center">
    <img
      @click="() => router.push({ name: 'ProductDetails', params: { supermarket: product.supermarket, productId: product.product_id } })"
      :src=product.image_url_s3 height="150" width="150" />
  <router-link :to="{ name: 'ProductDetails', params: { supermarket: product.supermarket, productId: product.product_id}}" style="text-decoration: none;">
    <ion-card-header class="ion-text-start"> 
      <ion-card-subtitle>
        <ion-text>{{ product.supermarket }}</ion-text>
      </ion-card-subtitle>
      <ion-card-title>
        <ion-text>
          <h5>{{ product.name }}</h5>
        </ion-text>
      </ion-card-title>
    </ion-card-header>
    </router-link>
    <ion-card-content class="ion-text-start">
      <ion-text><strong>{{ $filters.currency(product.prices[0].price) }}</strong></ion-text>
    </ion-card-content>
    <ion-grid>
      <ion-row class="ion-justify-content-around">
        <ion-col size-sm="4" size="3">
          <ion-button size="small" expand="block" shape="round" color="success"
            @click="!cart.isInShopList(product) && cart.addProduct(product) && toastProduct('Producto añadido a la cesta')">
            <ion-icon slot="icon-only" :icon="bagAdd"></ion-icon>
          </ion-button>
        </ion-col>
        <ion-col size="7">
          <ion-button size="small" expand="block" @click=" list.addProduct(product) && toastProduct('Producto añadido para comparar')">Comparar
          </ion-button>
        </ion-col>
      </ion-row>
    </ion-grid>
  </ion-card>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useListStore } from "@/store/list";
import { useCartStore } from "@/store/cart";
import {
  IonItem,
  IonCard,
  IonCardHeader,
  IonCardContent,
  IonCardTitle,
  IonCardSubtitle,
  IonText,
  IonButton,
  IonButtons,
  IonIcon,
  IonGrid,
  IonCol,
  IonRow,
  toastController
} from "@ionic/vue";
import { bagAdd } from "ionicons/icons";
import { useRouter } from "vue-router";

export default defineComponent({
  name: "ProductCard",
  components: {
    IonItem,
    IonCard,
    IonCardHeader,
    IonCardContent,
    IonCardTitle,
    IonCardSubtitle,
    IonText,
    IonButton,
    IonButtons,
    IonIcon,
    IonGrid,
    IonCol,
    IonRow
  },
  props: [
    "product"
  ],
  setup() {
    const router = useRouter();
    const list = useListStore();
    const cart = useCartStore();
    return {
      router,
      list,
      cart,
      bagAdd
    };
  },
  methods: {
    async toastProduct(message: string) {
      const toast = await toastController
        .create({
          message: message,
          duration: 500,
          color: 'tertiary',
          position: 'bottom'
        })
      return toast.present();
    },
  }
});
</script>

<style scoped>
ion-card-content {
  font-size: 20px;
}
</style>