<template>
  <ion-toolbar>
    <ion-grid>
      <ion-row>
        <ion-col>
          <ion-item style="margin-top: 11px">
            <ion-label>Supermercado</ion-label>
            <ion-select name="supermercado" multiple="true">
              <ion-select-option value="Dia">Dia</ion-select-option>
              <ion-select-option value="Carrefour">Carrefour</ion-select-option>
              <ion-select-option value="Consum">Consum</ion-select-option>
            </ion-select>
          </ion-item>
        </ion-col>
        <ion-col>
          <ion-item style="margin-top: 11px">
            <ion-label>Categoría</ion-label>
            <ion-select name="categoria" multiple="true">
              <ion-select-option value="Frutas">Frutas</ion-select-option>
              <ion-select-option value="Verduras">Verduras</ion-select-option>
              <ion-select-option value="Carne">Carne</ion-select-option>
            </ion-select>
          </ion-item>
        </ion-col>
        <ion-col>
          <ion-item style="height: 100%">
            <ion-label>Precio</ion-label>
            <ion-range dual-knobs pin color="tertiary" min="0" max="30">
              <ion-icon
                slot="start"
                size="small"
                :icon="cashOutline"
              ></ion-icon>
              <ion-icon slot="end" :icon="cashOutline"></ion-icon>
            </ion-range>
          </ion-item>
        </ion-col>
      </ion-row>
    </ion-grid>
  </ion-toolbar>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import {
  IonToolbar,
  IonItem,
  IonLabel,
  IonSelect,
  IonSelectOption,
} from "@ionic/vue";

import { cashOutline } from "ionicons/icons";

export default defineComponent({
  components: {
    IonToolbar,
    IonItem,
    IonLabel,
    IonSelect,
    IonSelectOption,
  },
  setup() {
    return {
      cashOutline,
    };
  },
});
</script>

<style scoped>
ion-range {
  --height: 1rem;
}
</style>
