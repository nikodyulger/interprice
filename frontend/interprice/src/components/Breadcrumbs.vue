<template>
    <div>
        <ion-chip outline>Frescos</ion-chip>
        <ion-chip outline> {{ category }} </ion-chip>
        <ion-chip outline v-if="subcategory"> {{ subcategory }} </ion-chip>
    </div>
</template>

<script lang="ts">
import {
    IonChip
} from '@ionic/vue';
import { defineComponent } from 'vue';
export default defineComponent({
    name: "Breadcrumbs",
    props: ['category', 'subcategory'],
    components: {
        IonChip
    }
})
</script>