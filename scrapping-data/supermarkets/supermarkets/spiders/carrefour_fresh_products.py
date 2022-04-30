from scrapy import Spider
from scrapy.http import JsonRequest
from ..items import ProductItem
from datetime import datetime 
from w3lib.html import remove_tags
import json


class carrefourSpider(Spider):
    name = 'Carrefour'
    allowed_domains = ['carrefour.es']
    start_urls = [
        'https://www.carrefour.es/cloud-api/plp-food-papi/v1/supermercado/productos-frescos/cat20002/c?offset={offset}']
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
            yield JsonRequest(url=self.start_urls[0].format(offset=24*i),
                            method='GET',
                            dont_filter=True,
                            callback=self.parse_products)

    def parse_products(self, response):
        data = json.loads(response.body)
        items = data['results']['items']

        for item in items:
            product_id = item['sku_id']
            name = item['name']
            price = item['price'].replace('€','').replace(',','.').strip()
            price = float(price)
            price_per_unit = item['price_per_unit'].replace('€','').replace(',','.').strip()
            price_per_unit = float(price_per_unit)
            url_img = item['images']['desktop']
            link = item['url']

            pr_info = {
                'product_id': int(product_id),
                'name': name,
                'price': price,
                'price_per_unit': price_per_unit,
                'url_img': [url_img]
            }

            yield response.follow(link,
                                  callback=self.parse_product_details,
                                  cb_kwargs=dict(pr_info=pr_info))

    def parse_product_details(self, response, pr_info):

        category = None
        subcategory = None
        ingredients = None
        storage = None
        preparation = None
        net_qty = None
        manufacturer = None

        breadcrumbs = response.css("li.breadcrumb__item > a::text").getall()

        if len(breadcrumbs) > 2:
            category = breadcrumbs[-2]
            subcategory = breadcrumbs[-1]

        if response.css("div.nutrition-ingredients__title:contains('Ingredientes')"):
            ingredients = remove_tags(response.css("p.nutrition-ingredients__content").get()).strip()

        if response.css("p.info-title:contains('Condiciones de conservación')"):
           storage = response.css("p.info-title:contains('Condiciones de conservación') + p::text").get().strip()

        if response.css("p.info-title:contains('Modo de empleo')"):
           preparation = response.css("p.info-title:contains('Modo de empleo') + p::text").get().strip()

        if response.css("span.nutrition-more-info__list-name:contains('Contenido neto')"):
            net_qty = response.css(
                "span.nutrition-more-info__list-name:contains('Contenido neto') + span::text").get().strip()

        if response.css("p.info-title:contains('Datos del producto')"):
            company_dir = response.css(
                "span.nutrition-more-info__list-name:contains('empresa') + span::text").get().strip()
            company_info = response.css(
                "span.nutrition-more-info__list-name:contains('fabricante') + span::text").get().strip()
            manufacturer = ' '.join([company_info, company_dir])

            yield ProductItem(product_id=pr_info['product_id'],
                              name=pr_info['name'],
                              supermarket=self.name,
                              category=category,
                              subcategory=subcategory,
                              price=pr_info['price'],
                              price_per_unit=pr_info['price_per_unit'],
                              net_qty=net_qty,
                              ingredients=ingredients,
                              storage=storage,
                              preparation=preparation,
                              manufacturer=manufacturer,
                              image_urls=pr_info['url_img'],
                              last_updated=datetime.today().strftime('%Y-%m-%d'))
