<script lang="ts">
import { defineComponent, h } from "vue";
import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale
} from "chart.js";

ChartJS.register(
  Title,
  Tooltip,
  LineElement,
  LinearScale,
  PointElement,
  CategoryScale
);

export default defineComponent({
  name: "PriceChart",
  components: {
    Line,
  },
  props: {
    width: {
      type: Number,
      default: 400,
    },
    height: {
      type: Number,
      default: 400,
    },
  },
  setup(props) {
    const chartData = {
      labels: ["January", "February", "March", "April", "May", "June", "July"],
      datasets: [
        {
          backgroundColor: "#f87979",
          data: [40, 39, 10, 40, 39, 80, 40],
        },
      ],
    };

    const chartOptions = {
      responsive: true,
      maintainAspectRatio: false,
    };
    
    return () =>
      h(Line, {
        chartData,
        chartOptions,
        width: props.width,
        height: props.height
      });
  },
});
</script>
