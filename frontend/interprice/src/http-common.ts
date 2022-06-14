import axios, { AxiosInstance } from "axios";

const api: AxiosInstance = axios.create({
    baseURL: process.env.VUE_APP_API_DOMAIN,
    headers: {
        "Content-type": "application/json",
    }
});

export default api;
