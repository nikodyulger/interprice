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
            </ion-list>
            <ion-grid>
                <ion-row>
                    <ion-col size-sm="6" size="6" class="ion-text-center">
                        <ion-button expand="block" class="ion-text-wrap" @click="copyToClipboard">
                            Copiar
                            <ion-icon slot="end" :icon="copyOutline"></ion-icon>
                        </ion-button>
                    </ion-col>
                    <ion-col size-sm="6" size="6" class="ion-text-center">
                        <ion-button expand="block" class="ion-text-wrap">
                            Compartir
                            <ion-icon slot="end" :icon="shareSocialOutline"></ion-icon>
                        </ion-button>
                    </ion-col>
                </ion-row>
            </ion-grid>
            <section>
            </section>
        </ion-card-content>
    </ion-card>
</template>
<script lang="ts">
import { defineComponent } from "vue";
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
    IonCol
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
            cb.writeText(JSON.stringify(this.products)).then(() => alert('Texto copiado!'));
        }
    }
});
</script>