<template>
    <ion-page>
        <Header/>
        <ion-content fullscreen>
            <ion-grid class="ion-padding ion-margin">
                <ion-row class="ion-content-justify-between">
                    <ion-col v-for="(products, supermarket) in cart.shoppingLists" :key="supermarket">
                        <ShopListCard :supermarket="supermarket" :products="products"/>
                    </ion-col>
                </ion-row>
            </ion-grid>
        </ion-content>
    </ion-page>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { useCartStore } from "@/store/cart";
import {
    IonPage,
    IonContent,
    IonGrid,
    IonRow,
    IonCol
} from "@ionic/vue";
import Header from "../components/Header.vue";
import ShopListCard from "../components/ShopListCard.vue";

export default defineComponent({
    name: "Cart",
    components: {
        IonPage,
        IonContent,
        IonGrid,
        IonRow,
        IonCol,
        Header,
        ShopListCard
    },
    setup(){
        const cart = useCartStore();
        return {
            cart
        }
    }
})
</script>
<style scoped>
ion-thumbnail {
    --size: px;
}

ion-card-content {
    overflow: visible;
}
</style>