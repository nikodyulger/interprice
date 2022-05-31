<template>
    <ion-fab vertical="bottom" horizontal="end" slot="fixed" class="ion-padding">
        <ion-badge color="danger" class="badge">{{list.numItems}}</ion-badge>
        <ion-fab-button color="secondary" @click="showModal">
            <ion-icon :icon="listOutline"></ion-icon>
        </ion-fab-button>
    </ion-fab>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useListStore } from "@/store/list";
import { listOutline } from "ionicons/icons";

import {
    IonBadge,
    IonFab,
    IonFabButton,
    IonIcon,
} from '@ionic/vue';

export default defineComponent({
    name: "Fab",
    components: {
        IonBadge,
        IonFab,
        IonFabButton,
        IonIcon,
    },
    setup() {
        const list = useListStore();
        return {
            list,
            listOutline
        }
    },
    methods: {
        showModal(){
            this.list.showList()
        }
    }
});
</script>
<style scoped>
.badge {
    left: 15px;
    z-index: 3;
    position: absolute;
}
</style>