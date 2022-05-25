import api from "@/http-common";

class API {
  getProducts(): Promise<any> {
    return api.get("/products");
  }

  getProductDetails(supermarket: string, productId: number): Promise<any> {
    return api.get(`/details/${supermarket}/${productId}`);
  }

  async getFilteredProducts(data: any): Promise<any> {
    const params = new URLSearchParams(data);
    return api.get("/products/filters/", {params: params});
  }
}

export default new API();
