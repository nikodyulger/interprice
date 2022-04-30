from scrapy import Spider
from scrapy.http import JsonRequest
from ..items import ProductItem
from datetime import datetime 
import json


class consumSpider(Spider):
    name = 'Consum'
    allowed_domains = ['.es']
    start_urls = [ 'https://tienda.consum.es/api/rest/V1.0/catalog/product?limit={limit}&offset={offset}&categories=2812']
    headers = {
        "x-tol-zone": "0"
    }
    custom_settings = {
        'FEED_URI' : 's3://supermarkets-interprice/data/%(name)s_%(time)s.json' ,
        'FEED_FORMAT' : 'json',
        'FEED_EXPORTERS': {
            'json' : 'scrapy.exporters.JsonItemExporter'
        }
    }
    def __init__(self, name=None, n_pages=2, **kwargs):
        super().__init__(name, **kwargs)
        self.n_pages = int(n_pages)

    def start_requests(self):
        for i in range(0,self.n_pages):
            yield JsonRequest(url=self.start_urls[0].format(limit=20,offset=20*i),
                            method='GET',
                            dont_filter=True,
                            headers=self.headers,
                            callback=self.parse_products)

    def parse_products(self, response):
        data = json.loads(response.body)
        items = data['products']

        for item in items:
            product_id = item['id']
            name = item['productData']['name']
            prices = item['priceData']['prices']

            for p in prices:
                if p['id'] == 'PRICE':
                    price = p['value']['centAmount']
                    price_per_unit = p['value']['centUnitAmount']

            url_img = item['productData']['imageURL']

            category = item['categories'][0]['name']

            yield ProductItem(product_id=product_id,
                              name=name,
                              supermarket=self.name,
                              category=category,
                              price=price,
                              price_per_unit=price_per_unit,
                              image_urls=[url_img],
                              last_updated=datetime.today().strftime('%Y-%m-%d'))
