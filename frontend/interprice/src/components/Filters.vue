<template>
  <ion-grid>
    <ion-row>
      <ion-searchbar color="light" enterkeyhint="enter" inputmode="search" type="search" @search="getSearchedProducts"
        v-model="search" placeholder="Busca productos" search-icon="search-outline" animated></ion-searchbar>
    </ion-row>
    <ion-row>
      <ion-toolbar>
        <ion-grid>
          <ion-row>
            <ion-col>
              <ion-item style="margin-top: 11px">
                <ion-label>Supermercado</ion-label>
                <ion-select name="supermarket" multiple="true" @ionChange="supermarketChanged">
                  <ion-select-option value="Dia">Dia</ion-select-option>
                  <ion-select-option value="Carrefour">Carrefour</ion-select-option>
                  <ion-select-option value="Consum">Consum</ion-select-option>
                </ion-select>
              </ion-item>
            </ion-col>
            <ion-col>
              <ion-item style="margin-top: 11px">
                <ion-label>Categoría</ion-label>
                <ion-select name="category" multiple="true" @ionChange="categoryChanged">
                  <ion-select-option value="Frutas">Frutas</ion-select-option>
                  <ion-select-option value="Verduras">Verduras</ion-select-option>
                  <ion-select-option value="Carne">Carne</ion-select-option>
                </ion-select>
              </ion-item>
            </ion-col>
            <ion-col>
              <ion-item style="height: 100%">
                <ion-label>Precio</ion-label>
                <ion-range dual-knobs pin color="tertiary" min="0" max="30" @ionChange="priceChanged">
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

        <ion-text color="primary" @click="orderBy('name')"><span>A-Z</span></ion-text>
        |
        <ion-text color="primary" @click="orderBy('price')"><span>Precio</span></ion-text>
      </ion-col>
    </ion-row>
  </ion-grid>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useCatalogStore } from "@/store/catalog";
import {
  IonSearchbar,
  IonToolbar,
  IonItem,
  IonLabel,
  IonSelect,
  IonSelectOption,
} from "@ionic/vue";

import { cashOutline } from "ionicons/icons";

export default defineComponent({
  components: {
    IonSearchbar,
    IonToolbar,
    IonItem,
    IonLabel,
    IonSelect,
    IonSelectOption,
  },
  data() {
    return {
      supermarkets: [],
      categories: [],
      prices: [],
      search: ""
    }
  },
  setup() {
    const store = useCatalogStore();

    const orderBy = (v: string) => {
      console.log(v)
      if (v === 'price') {
        store.orderByPrice();
      } else {
        store.orderByName();
      }
    };

    return {
      cashOutline,
      store,
      orderBy
    };
  },
  methods: {
    supermarketChanged(event: any) {
      console.log(event)
    },
    categoryChanged(event: any) {
      console.log(event)
    },
    priceChanged(event: any) {
      console.log(event)
    },
    getSearchedProducts(event: Event) {
      console.log(event);
      console.log(this.search);
      this.store.getSearchedProducts(this.search)
    },
  }
});
</script>

<style scoped>
ion-range {
  --height: 1rem;
}

.order span {
  display: inline-block;
  border-bottom: 2px solid;
  padding-bottom: 2px;
}
</style>
