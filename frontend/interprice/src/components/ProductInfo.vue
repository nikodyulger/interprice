<template>
    <ion-card style="height: 100%" class="product">
        <ion-grid>
            <ion-row>
                <ion-col offset="1">
                    <ion-thumbnail>
                        <ion-img :src=image_url_s3 />
                    </ion-thumbnail>
                </ion-col>
                <ion-col pull-sm="1">
                    <ion-text>
                        <h3>{{ supermarket }}</h3>
                    </ion-text>
                    <ion-card-title>
                        <ion-text>
                            <h1>{{ name }}</h1>
                        </ion-text>
                    </ion-card-title>
                    <ion-text>
                        <h5>{{ $filters.currencyWeight(prices[0].price_per_unit) }}</h5>
                    </ion-text>
                    <br />
                    <ion-text color="dark" class="price">
                        <strong>{{ $filters.currency(prices[0].price) }}</strong>
                    </ion-text>
                </ion-col>
            </ion-row>
        </ion-grid>
    </ion-card>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import {
    IonText,
    IonCard,
    IonCardTitle,
    IonCardHeader,
    IonGrid,
    IonRow,
    IonCol,
    IonThumbnail,
    IonImg
} from "@ionic/vue";

export default defineComponent({
    name: 'ProductInfo',
    props: ["product_id", "supermarket", "name", "image_url_s3", "prices"],
    components: {
        IonText,
        IonCard,
        IonCardTitle,
        IonCardHeader,
        IonGrid,
        IonRow,
        IonCol,
        IonThumbnail,
        IonImg
    }
});
</script>

<style scoped>
.price {
    font-size: 2rem;
}

.product {
    padding-top: 4rem;
    padding-bottom: 1.5rem;
}

ion-thumbnail {
    --size: 13rem;
}
</style>