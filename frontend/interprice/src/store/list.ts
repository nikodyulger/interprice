import { defineStore } from "pinia";
import { Product } from "../types/main";

export const useListStore = defineStore({
    id:'list',
    state: () => ({
        counter: 0,
        products: [] as Product[],
        show: false
    }),
    getters:{
        numItems(): number {
            return this.products.length;
        }
    },
    actions: {
        addProduct(product: any){
            this.products.push(product);
        },
        showList(){
            console.log(this.show)
            this.show = true;
        },
        hideList(){
            this.show = false;
        }
    }
});