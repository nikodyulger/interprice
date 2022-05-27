export interface Product {
    product_id: number;
    supermarket: string;
    name: string;
    category: string;
    image_url: string;
    image_url_s3: string;
    prices: any;
    details: any;
}

export interface Cart {
    [key: string]: Product[];
}