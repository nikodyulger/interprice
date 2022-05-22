<template>
  <ion-page>
    <Header />
    <ion-content fullscreen="true" class="ion-padding">
      <ion-grid>
        <ion-row>
          <ion-chip outline>Frescos</ion-chip>
          <ion-chip outline>Charcutería</ion-chip>
          <ion-chip outline>Salchichón, Salami y Fuet</ion-chip>
        </ion-row>
      </ion-grid>
      <ion-grid>
        <ion-row>
          <ion-col>
            <ion-card style="height: 100%" class="product">
                <ion-grid>
                  <ion-row >
                    <ion-col offset="1">
                      <ion-thumbnail>
                        <ion-img
                          src="https://static.carrefour.es/hd_350x_/img_pim_food/035834_00_1.jpg"
                        />
                      </ion-thumbnail>
                    </ion-col>
                    <ion-col pull-sm="1">
                      <ion-text><h3>Carrefour</h3></ion-text>
                      <ion-card-title>
                        <ion-text>
                          <h1>Banana a granel</h1>
                        </ion-text>
                      </ion-card-title>
                      <ion-text>
                        Cantidad Neta 700gr
                        <h5>1,25$/kg</h5>
                      </ion-text>
                      <br />
                      <ion-text color="dark" class="price">
                        <strong>1,25$</strong>
                      </ion-text>
                    </ion-col>
                  </ion-row>
                </ion-grid>
            </ion-card>
          </ion-col>
          <ion-col>
            <ion-card style="height: 100%" class="ion-padding">
              <ion-card-header>
                <ion-card-title
                  ><ion-text>Histórico de precios</ion-text></ion-card-title
                >
              </ion-card-header>
              <ion-card-content>
                <PriceChart />
              </ion-card-content>
            </ion-card>
          </ion-col>
        </ion-row>
      </ion-grid>
      <br />
      <ion-card>
        <ion-card-header>
          <ion-card-title><ion-text>Más información</ion-text></ion-card-title>
        </ion-card-header>
        <ion-card-content>
          <ion-list>
            <ion-item-group>
              <ion-item-divider mode="ios">
                <ion-label>Ingredientes</ion-label>
              </ion-item-divider>
            </ion-item-group>
            <ion-item lines="none"
              >Agua, quesos, mantequilla, leche desnatada en polvo, sales de
              fundido: polifosfatos, concentrado de minerales de la leche,
              concentrado de minerales de la leche, concentrado láctico lechero,
              sal
            </ion-item>
            <ion-item-group>
              <ion-item-divider mode="ios">
                <ion-label>Preparación</ion-label>
              </ion-item-divider>
            </ion-item-group>
            <ion-item lines="none"
              >Abrir el envase 10 minutos antes de su consumo.</ion-item
            >

            <ion-item-group>
              <ion-item-divider mode="ios">
                <ion-label>Conservación</ion-label>
              </ion-item-divider>
            </ion-item-group>
            <ion-item lines="none">Conservar entre +1 ºC y +4 ºC</ion-item>
            <ion-item-group>
              <ion-item-divider mode="ios">
                <ion-label>Fabricante</ion-label>
              </ion-item-divider>
            </ion-item-group>
            <ion-item lines="none"
              >CARREFOUR S.A. Calle La Estación, 2, 04640 Pulpí
              (Almería)</ion-item
            >
          </ion-list>
        </ion-card-content>
      </ion-card>
    </ion-content>
    <!-- <Footer /> -->
  </ion-page>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import {
  IonPage,
  IonCard,
  IonCardContent,
  IonCardHeader,
  IonCardSubtitle,
  IonCardTitle,
  IonGrid,
  IonRow,
  IonCol,
  IonItem,
  IonItemGroup,
  IonLabel,
  IonText,
  IonList,
  IonListHeader,
  IonChip,
  IonImg,
  IonThumbnail,
} from "@ionic/vue";
import Header from "../components/Header.vue";
import PriceChart from "../components/PriceChart.vue";

export default defineComponent({
  name: "ProductDetails",
  props: ["supermercado", "product_id"],
  components: {
    IonPage,
    IonCard,
    IonCardContent,
    IonCardHeader,
    IonCardSubtitle,
    IonCardTitle,
    IonGrid,
    IonRow,
    IonCol,
    IonItem,
    IonItemGroup,
    IonLabel,
    IonText,
    IonList,
    IonListHeader,
    IonChip,
    IonImg,
    IonThumbnail,
    Header,
    PriceChart,
  },
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
  --size: 15rem;
}
</style>