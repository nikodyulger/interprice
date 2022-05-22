<template>
  <ion-page>
    <Header />
    <br />
    <ion-content fullscreen class="ion-padding">
      <ion-grid>
        <ion-row>
          <ion-searchbar
            color="light"
            enterkeyhint="enter"
            inputmode="search"
            type="search"
            @search="getSearchedInput($event)"
            v-model="search"
            placeholder="Busca productos"
            search-icon="search-outline"
            animated
          ></ion-searchbar>
        </ion-row>
        <ion-row>
          <ion-col>
            <Filters />
          </ion-col>
        </ion-row>
        <ion-row class="ion-text-end">
          <ion-col pull="1">
            <ion-text>Ordenar por: </ion-text>

            <ion-text>A-Z</ion-text>
            |
            <ion-text>Precio</ion-text>
          </ion-col>
        </ion-row>
        <ion-row>
          <!-- <ion-col size="3">
          </ion-col> -->

          <ion-col>
            <ProductCard />
          </ion-col>
          <ion-col>
            <ProductCard />
          </ion-col>
          <ion-col>
            <ProductCard />
          </ion-col>
          <ion-col>
            <ProductCard />
          </ion-col>
          <ion-col>
            <ProductCard />
          </ion-col>
          <ion-col>
            <ProductCard />
          </ion-col>
        </ion-row>
        <ion-row>
          <PagesControl/>
        </ion-row>
      </ion-grid>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import axios from "axios";
import {
  IonPage,
  IonText,
  IonContent,
  IonGrid,
  IonRow,
  IonCol,
  IonSearchbar,
} from "@ionic/vue";

// import PromoListItem from "@/components/PromoListItem.vue";
import Header from "@/components/Header.vue";
import ProductCard from "@/components/ProductCard.vue";
import Filters from "@/components/Filters.vue";
import PagesControl from "@/components/PagesControl.vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "Home",
  data() {
    return {
      promos: null,
      search: "",
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/promos")
      .then((res) => (this.promos = res.data))
      .catch((err) => console.log(err.message));
  },
  components: {
    IonPage,
    IonText,
    IonContent,
    IonGrid,
    IonRow,
    IonCol,
    IonSearchbar,
    Header,
    Filters,
    ProductCard,
    PagesControl
  },
  methods: {
    getSearchedInput(event: Event) {
      console.log(event);
      console.log(this.search);
    },
  },
});
</script>
<style scoped>

</style>