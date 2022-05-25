import axios, { AxiosInstance } from "axios";

const api: AxiosInstance = axios.create({
    baseURL: "http://192.168.1.49:8000/",
    headers: {
        "Content-type": "application/json"
    }
});

export default api;
