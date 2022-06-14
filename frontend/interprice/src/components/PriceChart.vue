<template>
  <ion-card class="ion-padding" style="height: 100%;">
    <ion-card-header>
      <ion-card-title>
        <ion-text>Histórico de precios</ion-text>
      </ion-card-title>
    </ion-card-header>
    <ion-card-content>
      <Line :chart-data="chartData" :chart-options="chartOptions" :height="200" />
    </ion-card-content>
  </ion-card>
</template>

<script lang="ts">
import { defineComponent } from "vue";

import {
  IonCard,
  IonCardHeader,
  IonCardContent,
  IonCardTitle,
  IonText
} from "@ionic/vue";

import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale,
  Filler
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale,
  Filler
);

export default defineComponent({
  name: "PriceChart",
  components: {
    Line,
    IonCard,
    IonCardHeader,
    IonCardContent,
    IonCardTitle,
    IonText
  },
  props: ["prices"],
  computed: {
    labels() {
      return this.prices.map((p: any) => p.updated).reverse();
    },
    data() {
      return this.prices.map((p: any) => p.price).reverse();
    },
    chartData() {
      return {
        labels: this.labels,
        datasets: [
          {
            borderColor: '#5260ff',
            fill: true,
            tension: 0.2,
            data: this.data
          }
        ]
      }
    }
  },
  setup() {
    const chartOptions = {
      responsive: true,
      maintainAspectRatio: false
    };

    return {
      chartOptions
    }
  },
});
</script>
