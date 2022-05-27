import { defineStore } from "pinia";
import { Product } from "../types/main";
import API from "../services/apiService";

export const useCatalogStore = defineStore({
  id: "catalog",
  state: () => ({
    currentPage: 1,
    products: [] as Product[],
    catalog: [[]] as Product[][],
  }),
  getters: {
    pages(): number{
      return Math.ceil(this.products.length/30);
    },
    getProduct: (state) => {
      return (productId: number, supermarket: string) => {
        return state.products.find((p) => p.product_id === productId && p.supermarket === supermarket)
      }
    },
    filterByCategory: (state) => {
      return (filters: any) => {
        state.catalog = [[]];
        const prod = state.products.filter((p) => {
          let res = true

          if (filters.category.length > 0)
            res = res && filters.category.includes(p.category) 
            
          if(filters.supermarket.length > 0)
            res = res && filters.supermarket.includes(p.supermarket)
            

          // if(filters.price.length > 0)
          //   filters.price.includes(p.prices)
          return res
        }

        );
        for (let i = 0; i < prod.length; i += 6) {
          state.catalog.push(prod.slice(i, i + 6));
        }
      };
    },
  },
  actions: {
    orderByPrice() {
      this.products.sort((a, b) =>
        a.prices[0].price < b.prices[0].price ? -1 : 1
      );
      this.currentPage = 1;
      this.getCatalog();
    },
    orderByName() {
      this.products.sort((a, b) => (a.name < b.name ? -1 : 1));
      this.currentPage = 1;
      this.getCatalog();
    },
    getCatalog() {
      this.catalog = [[]];
      const prods = this.products.slice((this.currentPage - 1)*30, (this.currentPage - 1)*30 + 30)
      for (let i = 0; i < prods.length ; i += 6) {
        this.catalog.push(prods.slice(i, i + 6));
      }
    },
    nextPage(){
      this.currentPage += 1;
      this.getCatalog();
    },
    previousPage(){
      if(this.currentPage !== 1){
        this.currentPage -= 1;
      }
      this.getCatalog();
    },
    changePage(page: number){
      this.currentPage = page;
      this.getCatalog();
    },
    getProducts() {
      API.getProducts()
        .then((res) => {
          this.products = res.data;
          this.getCatalog();
        })
        .catch((err) => console.log(err.message));
    },
    getSearchedProducts(q: string){
      API.getSearchedProducts(q)
      .then((res) => {
        this.products = res.data;
        this.getCatalog();
      })
      .catch((err) => console.log(err.message));
    }
  },
});
