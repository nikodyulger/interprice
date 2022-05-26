<template>
  <keep-alive>
    <ion-page>
      <Header />
      <br />
      <ion-content fullscreen class="ion-padding ">
        <Filters />
        <ion-grid class="catalog">
          <ion-row v-for="row in catalog.catalog" :key="row">
            <ion-col v-for="prod in row" :key="prod.product_id" size-md="2">
              <ProductCard :name="prod.name" :productId="prod.product_id" :supermarket="prod.supermarket"
                :imageUrl="prod.image_url_s3" :price="prod.prices[0].price" />
            </ion-col>
          </ion-row>
        </ion-grid>
        <Fab />
        <ion-modal :is-open="list.show" @didDismiss="list.hideList">
          <Modal/>
        </ion-modal>
        <br />
        <br />
        <PagesControl />
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
  IonModal
} from "@ionic/vue";

import Header from "../components/Header.vue";
import ProductCard from "../components/ProductCard.vue";
import Filters from "../components/Filters.vue";
import PagesControl from "../components/PagesControl.vue";
import Fab from "../components/Fab.vue";
import Modal from "../components/Modal.vue";
import { defineComponent } from "vue";
import { useCatalogStore } from "@/store/catalog";
import { useListStore } from "@/store/list";

export default defineComponent({
  name: "Home",
  components: {
    IonPage,
    IonContent,
    IonGrid,
    IonRow,
    IonCol,
    IonModal,
    Header,
    Filters,
    Fab,
    Modal,
    ProductCard,
    PagesControl
  },
  methods: {

  },
  data() {
    return {
      search: "",
    };
  },
  beforeMount() {
    this.catalog.getProducts();
  },
  setup() {
    const catalog = useCatalogStore()
    const list = useListStore();
    // const catalog = computed(() => {
    //   const arr: Product[][] = [];
    //   for (let i = 0; i < store.products.length; i += 5) {
    //     arr.push(store.products.slice(i, i + 5))
    //   }
    //   return arr;
    // })

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
</style>