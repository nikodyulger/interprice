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
        },
        isInList: (state) => {
            return (product: Product) => {
                return state.products.indexOf(product) === -1 ? false : true;
            }
        }
    },
    actions: {
        addProduct(product: any){
            if(!this.isInList(product))
                this.products.push(product);
        },
        deleteProduct(product: any){
            const index = this.products.indexOf(product);
            this.products.splice(index,1);
        },
        deleteAll(){
            this.products = [];
        },
        showList(){
            this.show = true;
        },
        hideList(){
            this.show = false;
        }
    }
});