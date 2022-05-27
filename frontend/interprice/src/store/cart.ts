import { defineStore } from "pinia";
import { Cart } from "../types/main";

export const useCartStore = defineStore({
  id: "cart",
  state: () => ({
    shoppingLists: {} as Cart,
  }),
  getters: {
    hasSupermarket: (state) => {
      return (supermarket: string) => {
        return supermarket in state.shoppingLists;
      };
    },
    totalProducts(state) {
        let total = 0;
        for(const supermarket in state.shoppingLists ) {
            total += state.shoppingLists[supermarket].length;
        } 
        return total
    },
    isEmpty(state) {
        return Object.keys(state.shoppingLists).length === 0;
    },
    isInShopList: (state) => {
        return (product: any) => {
            return state.shoppingLists[product.supermarket].indexOf(product) === -1 ? false : true;
        }
    }
  },
  actions: {
    addProduct(product: any) {
      const supermarket = product.supermarket;
      this.hasSupermarket(supermarket) ? this.shoppingLists[supermarket].push(product) : (this.shoppingLists[supermarket] = [product])
      console.log(this.shoppingLists);
    },
  },
});
