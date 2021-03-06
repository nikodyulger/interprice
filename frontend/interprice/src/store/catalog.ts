import { defineStore } from "pinia";
import { Product } from "../types/main";
import API from "../services/apiService";

export const useCatalogStore = defineStore({
  id: "catalog",
  state: () => ({
    products: [] as Product[],
    filteredProducts: [] as Product[],
    catalog: [[]] as Product[][],
    currentPage: 1,
  }),
  getters: {
    pages(): number {
      return this.filteredProducts.length > 0
        ? Math.ceil(this.filteredProducts.length / 30)
        : Math.ceil(this.products.length / 30);
    },
    getProduct: (state) => {
      return (productId: number, supermarket: string) => {
        return state.products.find(
          (p) => p.product_id === productId && p.supermarket === supermarket
        );
      };
    },
    filterProducts: (state) => {
      return (filters: any) => {
        state.catalog = [[]];

        const prods = state.products.filter((p) => {
          let res = true;

          if (filters.categories.length > 0)
            res = res && filters.categories.includes(p.category);

          if (filters.supermarkets.length > 0)
            res = res && filters.supermarkets.includes(p.supermarket);

          if (Object.keys(filters.price).length === 2)
            res =
              res &&
              filters.price.lower <= p.prices[0].price &&
              p.prices[0].price <= filters.price.upper;

          return res;
        });

        for (let i = 0; i < prods.length; i += 5) {
          state.catalog.push(prods.slice(i, i + 5));
        }

        state.filteredProducts = prods;
        state.currentPage = 1;
      };
    },
  },
  actions: {
    orderByPrice() {
      this.filteredProducts.length > 0
        ? this.filteredProducts.sort((a, b) =>
            a.prices[0].price < b.prices[0].price ? -1 : 1
          )
        : this.products.sort((a, b) =>
            a.prices[0].price < b.prices[0].price ? -1 : 1
          );
      this.currentPage = 1;
      this.getCatalog();
    },
    orderByName() {
      this.filteredProducts.length > 0
        ? this.filteredProducts.sort((a, b) => (a.name < b.name ? -1 : 1))
        : this.products.sort((a, b) => (a.name < b.name ? -1 : 1));
      this.currentPage = 1;
      this.getCatalog();
    },
    getCatalog() {
      this.catalog = [[]];
      let prods = [];
      this.filteredProducts.length > 0
        ? (prods = this.filteredProducts.slice(
            (this.currentPage - 1) * 30,
            (this.currentPage - 1) * 30 + 30
          ))
        : (prods = this.products.slice(
            (this.currentPage - 1) * 30,
            (this.currentPage - 1) * 30 + 30
          ));

      for (let i = 0; i < prods.length; i += 5) {
        this.catalog.push(prods.slice(i, i + 5));
      }
    },
    nextPage() {
      if (this.currentPage !== this.pages) this.currentPage += 1;
      this.getCatalog();
    },
    previousPage() {
      if (this.currentPage !== 1) this.currentPage -= 1;
      this.getCatalog();
    },
    changePage(page: number) {
      this.currentPage = page;
      this.getCatalog();
    },
    getSearchedProducts(q: string) {
      API.getSearchedProducts(q)
        .then((res) => {
          this.products = res.data;
          this.filteredProducts = [];
          this.currentPage = 1;
          this.getCatalog();
        })
        .catch((err) => console.log(err.message));
    },
  },
});
