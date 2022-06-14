<template>
    <ion-page>
        <Header />
        <ion-content fullscreen>
            <ion-grid class="ion-padding ion-margin">
                <ion-row class="ion-justify-content-center">
                    <ion-card v-if="cart.isEmpty" class="ion-align-self-center">
                        <ion-card-header>
                            <ion-card-title>No hay listas de la compra!</ion-card-title>
                        </ion-card-header>
                    </ion-card>
                    <ion-col v-for="(products, supermarket) in cart.shoppingLists" :key="supermarket" size-sm="4">
                        <ShopListCard :supermarket="supermarket" :products="products" />
                    </ion-col>
                </ion-row>
            </ion-grid>
            <ion-modal :is-open="list.show" @didDismiss="list.hideList">
                <Modal />
            </ion-modal>
            <Fab />
            <Footer/>
        </ion-content>
    </ion-page>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import { useCartStore } from "@/store/cart";
import { useListStore } from "@/store/list";
import {
    IonPage,
    IonContent,
    IonGrid,
    IonRow,
    IonCol,
    IonCard,
    IonCardHeader,
    IonCardTitle,
    IonModal
} from "@ionic/vue";
import Header from "../components/Header.vue";
import ShopListCard from "../components/ShopListCard.vue";
import Fab from "../components/Fab.vue";
import Modal from "../components/Modal.vue";
import Footer from "../components/Footer.vue";

export default defineComponent({
    name: "Cart",
    components: {
        IonPage,
        IonContent,
        IonGrid,
        IonRow,
        IonCol,
        IonCard,
        IonCardHeader,
        IonCardTitle,
        IonModal,
        Header,
        ShopListCard,
        Fab,
        Modal,
        Footer
    },
    setup() {
        const cart = useCartStore();
        const list = useListStore();
        return {
            cart,
            list
        }
    }
})
</script>
<style scoped>
ion-card-content {
    overflow: visible;
}
</style>