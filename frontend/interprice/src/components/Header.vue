<template>
  <ion-header class="ion-no-border">
    <ion-toolbar color="tertiary">
      <ion-title slot="start">
        <ion-text @click="() => $route.name === 'Home' ? router.go(0) : router.push('/')">Interprice</ion-text>
      </ion-title>
      <ion-buttons slot="end" class="ion-margin-end">
        <ion-button size="large" shape="round" fill="clear" @click="() => router.push('/cart')">
          <ion-badge v-if="!cart.isEmpty" color="danger" class="badge">{{cart.totalProducts}}</ion-badge>
          <ion-icon slot="icon-only" :icon="cartOutline">
          </ion-icon>
        </ion-button>
      </ion-buttons>
    </ion-toolbar>
  </ion-header>
</template>

<script lang="ts">
import {
  IonHeader,
  IonToolbar,
  IonText,
  IonTitle,
  IonButtons,
  IonButton,
  IonBadge,
  IonIcon
} from "@ionic/vue";
import { cartOutline } from "ionicons/icons";
import { defineComponent } from "vue";
import { useRouter } from "vue-router";
import { useCartStore } from "@/store/cart";

export default defineComponent({
  components: {
    IonHeader,
    IonToolbar,
    IonText,
    IonTitle,
    IonButtons,
    IonButton,
    IonBadge,
    IonIcon,
  },
  data() {
    return {
      search: "",
    };
  },
  setup() {
    const router = useRouter();
    const cart = useCartStore();
    return {
      router,
      cart,
      cartOutline
    };
  },
});
</script>

<style scoped>
ion-button ion-badge {
  position: absolute;
  top: -8px;
  right: -5px;
  opacity: 0.9;
  font-size: small;
}
ion-toolbar{
  --min-height: 50px;
}
</style>