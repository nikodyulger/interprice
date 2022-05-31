<template>
  <ion-grid>
    <ion-row>
      <ion-searchbar color="light" enterkeyhint="search" inputmode="search" type="search" @search="getSearchedProducts"
        v-model="search" placeholder="Busca productos" search-icon="search-outline" animated clearIcon="close-sharp">
      </ion-searchbar>
    </ion-row>
    <ion-row>
      <ion-toolbar>
        <ion-grid>
          <ion-row>
            <ion-col>
              <ion-item style="margin-top: 11px">
                <ion-label>Supermercado</ion-label>
                <ion-select name="supermarket" multiple="true" @ionChange="supermarketChanged"
                  :value="filters.supermarkets">
                  <ion-select-option value="Dia">Dia</ion-select-option>
                  <ion-select-option value="Carrefour">Carrefour</ion-select-option>
                  <ion-select-option value="Consum">Consum</ion-select-option>
                </ion-select>
              </ion-item>
            </ion-col>
            <ion-col>
              <ion-item style="margin-top: 11px">
                <ion-label>Categoría</ion-label>
                <ion-select name="category" multiple="true" @ionChange="categoryChanged" :value="filters.categories">
                  <ion-select-option value="Frutas">Frutas</ion-select-option>
                  <ion-select-option value="Verduras">Verduras</ion-select-option>
                  <ion-select-option value="Carne">Carne</ion-select-option>
                </ion-select>
              </ion-item>
            </ion-col>
            <ion-col>
              <ion-item style="height: 100%">
                <ion-label>Precio</ion-label>
                <ion-range dual-knobs pin color="tertiary" min="0" max="20" debounce="150" @ionChange="priceChanged"
                  :value="initialPrice">
                  <ion-icon slot="start" size="small" :icon="cashOutline"></ion-icon>
                  <ion-icon slot="end" :icon="cashOutline"></ion-icon>
                </ion-range>
              </ion-item>
            </ion-col>
          </ion-row>
        </ion-grid>
      </ion-toolbar>
    </ion-row>
    <ion-row class="ion-text-end">
      <ion-col pull="1">
        <ion-text>Ordenar por: </ion-text>

        <ion-text color="primary" @click="orderBy('name')"><span :class="{ highlight: order === 'name' }">A-Z</span>
        </ion-text>
        |
        <ion-text color="primary" @click="orderBy('price')"><span
            :class="{ highlight: order === 'price' }">Precio</span>
        </ion-text>
      </ion-col>
    </ion-row>
  </ion-grid>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useCatalogStore } from "@/store/catalog";
import {
  IonGrid,
  IonRow,
  IonCol,
  IonSearchbar,
  IonToolbar,
  IonItem,
  IonLabel,
  IonSelect,
  IonSelectOption,
  IonRange,
  IonIcon,
  IonText,
loadingController
} from "@ionic/vue";

import { cashOutline } from "ionicons/icons";

export default defineComponent({
  components: {
    IonGrid,
    IonRow,
    IonCol,
    IonSearchbar,
    IonToolbar,
    IonItem,
    IonLabel,
    IonSelect,
    IonSelectOption,
    IonRange,
    IonIcon,
    IonText
  },
  data() {
    return {
      filters: {
        supermarkets: [],
        categories: [],
        price: {},
      },
      initialPrice: { lower: 0, upper: 20 },
      search: "",
      order: ""
    }
  },
  setup() {
    const store = useCatalogStore();

    return {
      cashOutline,
      store
    };
  },
  methods: {
    orderBy(v: string) {
      console.log(v)
      if (v === 'price') {
        this.store.orderByPrice();
        this.order = v;
      } else {
        this.store.orderByName();
        this.order = v;
      }
    },
    supermarketChanged(event: any) {
      this.filters.supermarkets = event.detail.value;
      this.store.filterProducts(this.filters);
    },
    categoryChanged(event: any) {
      this.filters.categories = event.detail.value;
      this.store.filterProducts(this.filters);
    },
    priceChanged(event: any) {
      this.filters.price = event.detail.value;
      this.store.filterProducts(this.filters);
    },
    getSearchedProducts() {
      this.presentLoading();
      this.filters.supermarkets = [];
      this.filters.categories = [];
      this.filters.price = this.initialPrice = { lower: 0, upper: 20 };
      this.order = "";
      this.store.getSearchedProducts(this.search);
    },
    async presentLoading() {
      const loading = await loadingController
      .create({
        message: "Por favor espere...",
        duration: 250
      });
      await loading.present();
    }
  }
});
</script>

<style scoped>
ion-range {
  --height: 30px;
}

.highlight {
  font-weight: bold;
  display: inline-block;
  border-bottom: 2px solid;
  padding-bottom: 2px;
}
</style>
