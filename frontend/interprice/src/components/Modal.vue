<template>
    <div>
        <ion-header>
            <ion-toolbar>
                <ion-item slot="start" lines="none">
                    <ion-icon :color="reorder ? 'dark' : 'tertiary'" :icon="reorderFourOutline"></ion-icon>
                    <ion-toggle color="tertiary" @click="toggleReorder"></ion-toggle>
                </ion-item>
                <ion-title>Lista</ion-title>
                <ion-buttons slot="end">

                    <ion-button size="large" shape="round" @click="list.hideList">
                        <ion-icon slot="icon-only" :icon="closeOutline"></ion-icon>
                    </ion-button>
                </ion-buttons>
            </ion-toolbar>
        </ion-header>
        <ion-content fullscreen>
            <ion-text v-if="list.products.length === 0" class="message">Añade productos para comparar!</ion-text>
            <ion-list v-if="list.products.length > 0">
                <ion-list-header>
                    <ion-label><strong>Comparativa</strong></ion-label>
                </ion-list-header>
                <ion-reorder-group :disabled="reorder" @ionItemReorder="reorderProducts($event)">
                    <ion-reorder v-for="p in list.products" :key="p.product_id">
                        <ion-item>
                            <ion-thumbnail class="ion-margin">
                                <ion-img :src="p.image_url_s3"></ion-img>
                            </ion-thumbnail>
                            <ion-label>
                                <h2>{{ p.name }}</h2>
                                <h3>{{ p.supermarket }}</h3>
                                <p>{{ $filters.currency(p.prices[0].price) }}</p>
                            </ion-label>
                            <ion-button color="success" shape="round" @click="addProduct(p)">
                                <ion-icon slot="icon-only" :icon="checkmarkCircleOutline"></ion-icon>
                            </ion-button>
                            <ion-button color="danger" shape="round" @click="deleteProduct(p)">
                                <ion-icon slot="icon-only" :icon="closeCircleOutline"></ion-icon>
                            </ion-button>
                        </ion-item>
                    </ion-reorder>
                </ion-reorder-group>
            </ion-list>
            <section class="ion-padding ion-text-center" v-if="list.products.length > 0">
                <ion-button color="danger" fill="outline" @click="list.deleteAll()">
                    <ion-icon :icon="trashOutline"></ion-icon>
                    <ion-text>Eliminar todos</ion-text>
                </ion-button>
            </section>
        </ion-content>
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useListStore } from "@/store/list";
import { useCartStore } from "@/store/cart";

import {
    IonHeader,
    IonTitle,
    IonToolbar,
    IonIcon,
    IonButtons,
    IonButton,
    IonContent,
    IonLabel,
    IonList,
    IonListHeader,
    IonItem,
    IonThumbnail,
    IonImg,
    IonText,
    IonReorder,
    IonReorderGroup,
    IonToggle,
    toastController
} from "@ionic/vue";

import { closeOutline, checkmarkCircleOutline, closeCircleOutline, trashOutline, reorderFourOutline } from "ionicons/icons";
export default defineComponent({
    name: "Modal",
    components: {
        IonHeader,
        IonTitle,
        IonToolbar,
        IonIcon,
        IonButtons,
        IonButton,
        IonContent,
        IonLabel,
        IonList,
        IonListHeader,
        IonItem,
        IonThumbnail,
        IonImg,
        IonText,
        IonReorder,
        IonReorderGroup,
        IonToggle
    },
    data() {
        return {
            reorder: true
        }
    },
    setup() {
        const list = useListStore();
        const cart = useCartStore();
        return {
            list,
            cart,
            closeOutline,
            checkmarkCircleOutline,
            closeCircleOutline,
            trashOutline,
            reorderFourOutline
        }
    },
    methods: {
        addProduct(product: any) {
            if (!this.cart.isInShopList(product)) {
                this.cart.addProduct(product);
                this.list.deleteProduct(product);
                this.toastProduct('Producto añadido a la cesta', 'tertiary');
            }
        },
        deleteProduct(product: any) {
            this.list.deleteProduct(product);
            this.toastProduct('Producto descartado', 'danger');
        },
        reorderProducts(event: any) {
            event.detail.complete()
        },
        toggleReorder() {
            console.log(this.reorder);
            this.reorder = !this.reorder;
            console.log(this.reorder);
        },
        async toastProduct(message: string, color: string) {
            const toast = await toastController
                .create({
                    message: message,
                    duration: 500,
                    color: color,
                    position: 'bottom'
                })
            return toast.present();
        },
    }
});
</script>
<style scoped>
ion-title {
    text-align: center;
}

.message {
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}
</style>