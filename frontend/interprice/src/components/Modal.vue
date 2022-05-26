<template>
    <div>
        <ion-header>
            <ion-toolbar>
                <ion-title>Lista</ion-title>
                <ion-buttons slot="end">
                    <ion-button size="large" shape="round" @click="list.hideList">
                        <ion-icon slot="icon-only" :icon="closeOutline"></ion-icon>
                    </ion-button>
                </ion-buttons>
            </ion-toolbar>
        </ion-header>
        <ion-content fullscreen>
            <ion-list>
                <ion-item v-for="p in list.products" :key="p.product_id">
                    <ion-thumbnail class="ion-margin">
                        <ion-img :src="p.image_url_s3"></ion-img>
                    </ion-thumbnail>
                    <ion-label>
                        <h2>{{ p.name }}</h2>
                        <h3>{{p.supermarket}}</h3>
                        <p>{{ $filters.currency(p.prices[0].price)}}</p>
                    </ion-label>
                    <ion-button color="success" shape="round">
                        <ion-icon slot="icon-only" :icon="checkmarkCircleOutline"></ion-icon>
                    </ion-button>
                    <ion-button color="danger" shape="round">
                        <ion-icon slot="icon-only" :icon="checkmarkCircleOutline"></ion-icon>
                    </ion-button>
                </ion-item>
            </ion-list>
        </ion-content>
    </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useListStore } from "@/store/list";
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
    IonItem,
    IonThumbnail,
    IonImg
} from "@ionic/vue";
import { closeOutline, checkmarkCircleOutline } from "ionicons/icons";
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
        IonItem,
        IonThumbnail,
        IonImg
    },
    setup() {
        const list = useListStore();
        return {
            list,
            closeOutline,
            checkmarkCircleOutline
        }
    }
});
</script>
<style scoped>
ion-title {
    text-align: center;
}
</style>