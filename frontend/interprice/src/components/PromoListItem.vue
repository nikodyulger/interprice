<template>
  <ion-item v-if="promo" class="list-item item-thum">
    <ion-thumbnail slot="start">
      <ion-img :src=promo.url ></ion-img>
    </ion-thumbnail>
    <ion-label class="ion-text-wrap">
      <h2>
        {{ promo.name }}
      </h2>
      <p>{{ promo.price }}</p>
    </ion-label>
  </ion-item>
</template>

<script lang="ts">
import { IonItem, IonLabel, IonThumbnail, IonImg } from "@ionic/vue";
import { defineComponent } from "vue";

export default defineComponent({
  name: "PromoListItem",
  components: {
    IonItem,
    IonLabel,
    IonThumbnail,
    IonImg
  },
  props: {
    promo: Object,
  },
  methods: {
    isIos: () => {
      const win = window as any;
      return win && win.Ionic && win.Ionic.mode === "ios";
    },
  },
});
</script>

<style scoped>
.list-item {
  --padding-start: 0;
  --inner-padding-end: 0;
}

.list-item ion-label {
  margin-top: 12px;
  margin-bottom: 12px;
}

.list-item h2 {
  font-weight: 600;
  margin: 0;
}

.list-item p {
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  width: 95%;
}

.list-item .date {
  float: right;
  align-items: center;
  display: flex;
}

.list-item ion-icon {
  color: #c9c9ca;
}

.list-item ion-note {
  font-size: 15px;
  margin-right: 8px;
  font-weight: normal;
}

.list-item ion-note.md {
  margin-right: 14px;
}

.list-item .dot {
  display: block;
  height: 12px;
  width: 12px;
  border-radius: 50%;
  align-self: start;
  margin: 16px 10px 16px 16px;
}

.list-item .dot-unread {
  background: var(--ion-color-primary);
}
</style>