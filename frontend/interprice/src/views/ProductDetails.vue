<template>
  <ion-page>
    <Header />
    <ion-content fullscreen="true" class="ion-padding">
      <ion-loading :is-open="!loading" message="Por favor, espere..."></ion-loading>
      <ion-grid>
        <ion-row>
          <Breadcrumbs v-if="loading" :category="product.category"
            :subcategory="product.details ? product.details.subcategory : ''" />
        </ion-row>
      </ion-grid>
      <ion-grid>
        <ion-row>
          <ion-col>
            <ProductInfo v-if="loading" v-bind="product" />
          </ion-col>
          <ion-col>
            <ion-card style="height: 100%" class="ion-padding">
              <ion-card-header>
                <ion-card-title>
                  <ion-text>Histórico de precios</ion-text>
                </ion-card-title>
              </ion-card-header>
              <ion-card-content>
                <PriceChart />
              </ion-card-content>
            </ion-card>
          </ion-col>
        </ion-row>
      </ion-grid>
      <br />
      <DetailInfo v-if="product.details" v-bind="product.details" />
      <ion-modal :is-open="list.show" @didDismiss="list.hideList">
        <Modal />
      </ion-modal>
      <Fab />
      <Footer />
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import { useListStore } from "@/store/list";
import {
  IonPage,
  IonContent,
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonCardSubtitle,
  IonCardTitle,
  IonGrid,
  IonRow,
  IonCol,
  IonText,
  IonLoading,
  IonModal
} from "@ionic/vue";
import Header from "../components/Header.vue";
import PriceChart from "../components/PriceChart.vue";
import ProductInfo from "../components/ProductInfo.vue";
import Breadcrumbs from "../components/Breadcrumbs.vue";
import DetailInfo from "../components/DetailInfo.vue";
import Modal from "../components/Modal.vue";
import Fab from "../components/Fab.vue";
import Footer from "../components/Footer.vue";
import { Product } from "../types/main";
import API from "../services/apiService";

export default defineComponent({
  name: "ProductDetails",
  props: ["supermarket", "productId"],
  components: {
    IonPage,
    IonContent,
    IonCard,
    IonCardContent,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
    IonGrid,
    IonRow,
    IonCol,
    IonText,
    IonLoading,
    IonModal,
    Header,
    PriceChart,
    ProductInfo,
    Breadcrumbs,
    DetailInfo,
    Modal,
    Fab,
    Footer
  },
  data() {
    return {
      loading: false,
      product: {} as Product
    }
  },
  setup(){
    const list = useListStore();
    return {
      list
    }
  },
  mounted() {
    API.getProductDetails(this.supermarket, this.productId)
      .then((res) => {
        this.product = res.data;
        this.loading = true;
      })
      .catch((err) => console.log(err.message));
  }
});
</script>
<style scoped>
</style>