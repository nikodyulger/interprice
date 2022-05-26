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
    }
  //   filterByCategory: (state) => {
  //     return (categories: string[]) => {
  //       state.catalog = [[]];
  //       state.filteredProducts = state.products.filter((p) =>
  //         categories.includes(p.category)
  //       );
  //       console.log(state.filteredProducts);
  //       for (let i = 0; i < state.filteredProducts.length; i += 6) {
  //         state.catalog.push(state.filteredProducts.slice(i, i + 6));
  //       }
  //     };
  //   },
  },
  actions: {
    orderByPrice() {
      this.products.sort((a, b) =>
        a.prices[0].price < b.prices[0].price ? -1 : 1
      );
      this.getCatalog();
    },
    orderByName() {
      this.products.sort((a, b) => (a.name < b.name ? -1 : 1));
      this.getCatalog();
    },
    getCatalog() {
      this.catalog = [[]];
      console.log((this.currentPage - 1)*30,(this.currentPage - 1)*30 + 30 )
      const prods = this.products.slice((this.currentPage - 1)*30, (this.currentPage - 1)*30 + 30)
      console.log(prods)
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
