<template>
    <ion-footer collapse="fade">
        <ion-toolbar class="ion-text-center">
            <ion-buttons slot="start">
                <ion-button>
                    <ion-icon slot="icon-only" :icon="logoGithub" href="'https://github.com/nikodyulger/interprice'" />
                </ion-button>
            </ion-buttons>
            <ion-title size="small">Prototipo app</ion-title>
        </ion-toolbar>
    </ion-footer>
</template>
<script lang="ts">
import { defineComponent } from "vue";
import {
    IonFooter,
    IonToolbar,
    IonButtons,
    IonButton,
    IonTitle,
    IonIcon
} from "@ionic/vue";

import { logoGithub } from "ionicons/icons";

export default defineComponent({
    name: "Footer",
    components: {
        IonFooter,
        IonToolbar,
        IonButtons,
        IonButton,
        IonTitle,
        IonIcon
    },
    setup() {
        return {
            logoGithub
        }
    }
});
</script>

<style scoped>
ion-toolbar {
    --min-height: 65px;
}
</style>