import api from "@/http-common";

class API {
  getProducts(): Promise<any> {
    return api.get("/products");
  }

  getProductDetails(supermarket: string, productId: number): Promise<any> {
    return api.get(`/details/${supermarket}/${productId}`);
  }

  getSearchedProducts(q: string): Promise<any> {
    return api.get(`/products/search/?q=${q}`);
  }

  sendSMS(sms: any) {
    return api.post('/sendsms',sms);
  }

  verifyPhone(verifySMS: any){
    return api.post('/verifyphone', verifySMS)
  }
}

export default new API();
