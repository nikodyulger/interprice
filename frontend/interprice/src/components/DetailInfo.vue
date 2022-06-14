<template>
    <ion-card v-if="!isEmpty">
        <ion-card-header>
            <ion-card-title>
                <ion-text>Más información</ion-text>
            </ion-card-title>
        </ion-card-header>
        <ion-card-content>
            <ion-list>
                <ion-item-group v-if=ingredients>
                    <ion-item-divider mode="ios">
                        <ion-label>Ingredientes</ion-label>
                    </ion-item-divider>
                    <ion-item lines="none">
                        {{ ingredients }}
                    </ion-item>
                </ion-item-group>

                <ion-item-group v-if=preparation>
                    <ion-item-divider mode="ios">
                        <ion-label>Preparación</ion-label>
                    </ion-item-divider>
                    <ion-item lines="none">
                        {{ preparation }}
                    </ion-item>
                </ion-item-group>

                <ion-item-group v-if=storage>
                    <ion-item-divider mode="ios">
                        <ion-label>Conservación</ion-label>
                    </ion-item-divider>
                    <ion-item lines="none">
                        {{ storage }}
                    </ion-item>
                </ion-item-group>

                <ion-item-group>
                    <ion-item-divider mode="ios" v-if=manufacturer>
                        <ion-label>Fabricante</ion-label>
                    </ion-item-divider>
                    <ion-item lines="none">
                        {{ manufacturer }}
                    </ion-item>
                </ion-item-group>
            </ion-list>
        </ion-card-content>
    </ion-card>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

import {
    IonCard,
    IonCardContent,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
    IonItem,
    IonItemGroup,
    IonItemDivider,
    IonLabel,
    IonText,
    IonList,
} from "@ionic/vue";

export default defineComponent({
    name: "Breadcrumbs",
    props: {
        ingredients: String,
        preparation: String,
        storage: String,
        manufacturer: String
    },
    components: {
        IonCard,
        IonCardContent,
        IonCardHeader,
        IonCardSubtitle,
        IonCardTitle,
        IonItem,
        IonItemGroup,
        IonItemDivider,
        IonLabel,
        IonText,
        IonList,
    },
    computed: {
        isEmpty(): boolean {
            return Object.values(this.$props).every(p => p === null || p === '');
        }
    }
})
</script>