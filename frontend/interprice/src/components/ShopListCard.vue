<template>
    <ion-card>
        <ion-card-header class="ion-text-center">
            <ion-card-title>{{ supermarket }}</ion-card-title>
        </ion-card-header>
        <ion-card-content>
            <ion-list>
                <ion-list-header>
                    <ion-label>Lista</ion-label>
                </ion-list-header>
                <ion-item v-for="p in products" :key="p.product_id">
                    <ion-label>
                        {{ p.name }}
                    </ion-label>
                    <ion-note slot="end">{{ $filters.currency(p.prices[0].price) }}</ion-note>
                </ion-item>
                <ion-item>
                    <ion-label slot="end"><strong>Total: </strong>{{ $filters.currency(totalShoppingList) }}</ion-label>
                </ion-item>
            </ion-list>
            <ion-grid>
                <ion-row>
                    <ion-col size-sm="6" size="6" class="ion-text-center">
                        <ion-button expand="block" color="medium" class="ion-text-wrap" @click="copyToClipboard">

                            <ion-icon slot="icon-only" :icon="copyOutline"></ion-icon>
                        </ion-button>
                    </ion-col>
                    <ion-col size-sm="6" size="6" class="ion-text-center">
                        <ion-button expand="block" color="tertiary" class="ion-text-wrap" @click="alertSendSMS">

                            <ion-icon slot="icon-only" :icon="shareSocialOutline"></ion-icon>
                        </ion-button>
                    </ion-col>
                </ion-row>
            </ion-grid>
        </ion-card-content>
    </ion-card>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import API from "../services/apiService";
import { Product } from "../types/main";

import {
    IonCard,
    IonCardContent,
    IonCardHeader,
    IonCardTitle,
    IonCardSubtitle,
    IonList,
    IonListHeader,
    IonItem,
    IonNote,
    IonLabel,
    IonIcon,
    IonButton,
    IonGrid,
    IonRow,
    IonCol,
    toastController,
    alertController
} from "@ionic/vue";
import { shareSocialOutline, copyOutline } from "ionicons/icons";

export default defineComponent({
    name: "ShopListCard",
    components: {
        IonCard,
        IonCardContent,
        IonCardHeader,
        IonCardTitle,
        IonCardSubtitle,
        IonList,
        IonListHeader,
        IonItem,
        IonNote,
        IonLabel,
        IonIcon,
        IonButton,
        IonGrid,
        IonRow,
        IonCol
    },
    props: ["supermarket", "products"],
    setup() {
        return {
            shareSocialOutline,
            copyOutline
        }
    },
    methods: {
        copyToClipboard() {
            const cb = navigator.clipboard;
            cb.writeText(this.textMessage)
                .then(() => this.toastMessage('Texto copiado!', 'tertiary'));
        },
        sendSMS(phoneNumber: number, message: string) {
            return API.sendSMS({
                number: `+34${phoneNumber}`,
                message: message
            }).then((res) => {
                res.data === 'Verified' ? this.toastMessage('Mensaje SMS enviado!', 'tertiary') : this.toastMessage('Tu número no está verificado!', 'danger');
            });
        },
        async alertSendSMS() {
            const alert = await alertController.create({
                header: "Compartir por SMS",
                message: "Introduce tu número de teléfono",
                inputs: [
                    {
                        name: 'tel',
                        type: 'tel',
                        placeholder: 'Teléfono'
                    }],
                buttons: [
                    {
                        text: 'Cancelar',
                        role: 'cancel',
                        cssClass: 'secondary',
                        handler: () => {
                           this.toastMessage('Operación cancelada!','danger');
                        }
                    }, {
                        text: 'Ok',
                        handler: (inputs) => {
                            this.sendSMS(inputs.tel, this.textMessage)
                        }
                    }
                ]
            });
            await alert.present();
        },
        async toastMessage(message: string, color: string) {
            const toast = await toastController
                .create({
                    message: message,
                    duration: 500,
                    color: color,
                    position: 'bottom'
                })
            return toast.present();
        },
    },
    computed: {
        totalShoppingList() {
            return this.products.reduce((acc: number, p: Product) => acc + p.prices[0].price, 0);
        },
        textMessage() {
            return JSON.stringify(this.products.map((p: any) => { return { name: p.name, price: p.prices[0].price } }));
        }
    }
});
</script>
<style scoped>
ion-note {
    font-size: small;
}
</style>