<template>
  <ion-card class="ion-text-center">
    <img
      @click="() => router.push({ name: 'ProductDetails', params: { supermarket: supermarket, productId: productId } })"
      :src=imageUrl height="150" width="150" />
    <ion-card-header class="ion-text-start" button
      router-link="{ name: 'ProductDetails', params: { supermarket: supermarket, productId: productId}}">
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
    <ion-grid>
      <ion-row class="ion-justify-content-around">
        <ion-col size-sm="4" size="4" class="ion-text-center">
          <ion-button size="small" expand="block" shape="round" color="success" @click="addProductToCart">
            <ion-icon slot="icon-only" :icon="bagAdd"></ion-icon>
          </ion-button>
        </ion-col>
        <ion-col size-sm="6" size="6" class="ion-text-center">
          <ion-button size="small" expand="block" @click="addProductToList">Comparar</ion-button>
        </ion-col>
      </ion-row>
    </ion-grid>
  </ion-card>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useListStore } from "@/store/list";
import { useCatalogStore } from "@/store/catalog";
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
  IonRow
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
    "productId", "supermarket", "name", "imageUrl", "price",
  ],
  setup() {
    const router = useRouter();
    const list = useListStore();
    const catalog = useCatalogStore();
    const cart = useCartStore();
    return {
      router,
      list,
      catalog,
      cart,
      bagAdd
    };
  },
  methods: {
    addProductToCart() {
      const prod = this.catalog.getProduct(this.$props.productId, this.$props.supermarket);
      this.cart.addProduct(prod);
    },
    addProductToList() {
      const prod = this.catalog.getProduct(this.$props.productId, this.$props.supermarket);
      this.list.addProduct(prod);
    }
  }
});
</script>

<style scoped>
ion-card-content {
  font-size: 20px;
}
</style>