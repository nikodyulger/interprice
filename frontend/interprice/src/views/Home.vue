<template>
  <keep-alive>
    <ion-page>
      <Header />
      <br />
      <ion-content fullscreen class="ion-padding">
        <ion-loading :is-open="loading" message="Por favor, espere ..."/>
        <Filters />
        <ion-grid>
          <ion-row v-for="row in catalog.catalog" :key="row" class="ion-justify-content-center">
            <ion-col v-for="prod in row" :key="prod.product_id" size-sm="2">
              <ProductCard :product="prod" />
            </ion-col>
          </ion-row>
        </ion-grid>
        <Fab />
        <ion-modal :is-open="list.show" @didDismiss="list.hideList">
          <Modal />
        </ion-modal>
        <br />
        <PagesControl />
        <br/>
        <Footer />
      </ion-content>
    </ion-page>
  </keep-alive>
</template>

<script lang="ts">
import {
  IonPage,
  IonContent,
  IonGrid,
  IonRow,
  IonCol,
  IonModal,
  IonLoading
} from "@ionic/vue";

import Header from "../components/Header.vue";
import ProductCard from "../components/ProductCard.vue";
import Filters from "../components/Filters.vue";
import PagesControl from "../components/PagesControl.vue";
import Fab from "../components/Fab.vue";
import Modal from "../components/Modal.vue";
import Footer from "../components/Footer.vue";
import { defineComponent } from "vue";
import { useCatalogStore } from "@/store/catalog";
import { useListStore } from "@/store/list";
import API from "../services/apiService";

export default defineComponent({
  name: "Home",
  components: {
    IonPage,
    IonContent,
    IonGrid,
    IonRow,
    IonCol,
    IonModal,
    IonLoading,
    Header,
    Filters,
    Fab,
    Modal,
    ProductCard,
    PagesControl,
    Footer
  },
  methods: {

  },
  data() {
    return {
      loading: true
    };
  },
  mounted() {
    if (this.catalog.products.length === 0) {
      API.getProducts()
        .then((res) => {
          this.catalog.products = res.data;
          this.catalog.getCatalog();
          console.log(res);
        })
        .catch((err) => console.log(err));
    }
    this.loading = false;
  },

  setup() {
    const catalog = useCatalogStore()
    const list = useListStore();

    return {
      catalog,
      list
    }
  }
});
</script>
<style scoped>
ion-card {
  padding: 5px;
}

ion-page {
  margin-bottom: 40px;
}

</style>