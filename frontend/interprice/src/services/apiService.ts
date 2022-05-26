import api from "@/http-common";

class API {
  getProducts(): Promise<any> {
    return api.get("/products");
  }

  getProductDetails(supermarket: string, productId: number): Promise<any> {
    return api.get(`/details/${supermarket}/${productId}`);
  }

  async getSearchedProducts(q: string): Promise<any> {
    return api.get(`/products/search/?q=${q}`);
  }
}

export default new API();
