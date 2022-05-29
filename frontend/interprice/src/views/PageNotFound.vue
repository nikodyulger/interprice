<template>
    <ion-page>
        <ion-content fullscreen>
            <ion-card class="ion-align-self-center">
                <ion-card-header>
                    <ion-card-subtitle>Error 404</ion-card-subtitle>
                    <ion-card-title>Página no encontrada!</ion-card-title>
                </ion-card-header>
            </ion-card>
        </ion-content>
    </ion-page>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import {
    IonPage,
    IonContent,
    IonCard,
    IonCardHeader,
    IonCardTitle,
    IonCardSubtitle
} from "@ionic/vue";
export default defineComponent({
    name: "PageNotFound",
    components: {
        IonPage,
        IonContent,
        IonCard,
        IonCardHeader,
        IonCardTitle,
        IonCardSubtitle
    }
})
</script>
<style scoped>
.message {
    position: absolute;
    left: 50%;
    top: 25%;
    transform: translate(-25%, -25%);
}
</style>