from scrapy import Spider, Request
from ..items import ProductItem
from datetime import datetime
from w3lib.html import remove_tags
import re
import requests
import time


class diaSpider(Spider):
    name = 'Dia'
    allowed_domains = ['dia.es']
    start_urls = ['https://www.dia.es/compra-online/frescos/cf/',
                  'https://www.dia.es/compra-online/frescos/cf?page={page}&disp=']
    custom_settings = {
        'FEED_URI': 's3://supermarkets-interprice/data/%(name)s_%(time)s.json',
        'FEED_FORMAT': 'json',
        'FEED_EXPORTERS': {
            'json': 'scrapy.exporters.JsonItemExporter'
        }
    }

    def __init__(self, name=None, n_pages=2, **kwargs):
        super().__init__(name, **kwargs)
        self.n_pages = int(n_pages)

    def start_requests(self):
        yield Request(url=self.start_urls[0],
                      callback=self.parse_products)
        for i in range(1, self.n_pages):
            yield Request(url=self.start_urls[1].format(page=i),
                          callback=self.parse_products)

    def parse_products(self, response):
        products = response.css("div.product-list__item")

        for pr in products:

            name = pr.css("span.details::text").get().strip()
            price = pr.css("p.price::text").get().replace(
                '€', '').replace(',', '.').strip()
            price = float(price)

            try:
                price_per_unit = pr.css("p.pricePerKilogram::text").get().replace(
                    u'\xa0', '').replace('€/Kg.', '').replace(',', '.').strip()
                price_per_unit = float(price_per_unit)
            except ValueError:
                price_per_unit = pr.css("p.pricePerKilogram::text").get().replace(
                    u'\xa0', '').replace('€/ud.', '').replace(',', '.').strip()
                price_per_unit = float(price_per_unit)

            url_img = pr.css("img.crispImage::attr(src)").get()
            link = pr.css('a.productMainLink::attr(href)').get()

            pr_info = {
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

        product_id = response.url.split('/')[-1]

        breadcrumbs = response.css("li[itemprop = 'itemListElement']")[-2:]

        if len(breadcrumbs) == 2:
            category = breadcrumbs[0].css(
                "span[itemprop='name']::text").get().strip()
            subcategory = breadcrumbs[1].css(
                "span[itemprop='name']::text").get().strip()

        add_info = response.css('div.product-nutritional-info')

        if add_info:

            if add_info.css("h4:contains('Ingredientes')"):
                ingredients = remove_tags(add_info.css(
                    "h4:contains('Ingredientes') + div.form_field-label").get()).strip()

            if add_info.css("h4:contains('Condiciones de conservación')"):
                storage = add_info.css(
                    "h4:contains('Condiciones de consergvación') + div.form_field-label").get()

            if add_info.css("h4:contains('Modo de Empleo')"):
                preparation = add_info.css(
                    "h4:contains('Modo de Empleo') + div::text").get().strip()

            if add_info.css("div:contains('CANTIDAD NETA (en masa)')"):
                net_qty = add_info.css(
                    "div:contains('CANTIDAD NETA (en masa)') + div::text").get().replace(u'\xa0', ' ').strip()

            if add_info.css("h4:contains('Manufacturado')"):
                company_info = add_info.css(
                    "div.tabs-nutritionalinfo-row-div::text").getall()
                company_info = [re.sub(r'\s+', ' ', ci.strip())
                                for ci in company_info]
                manufacturer = ' '.join(company_info)

        yield ProductItem(product_id=int(product_id),
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

    def closed(self, reason):
        time.sleep(10)
        if reason == 'finished':
            requests.get('https://lqt7l5fcxpnnmiv5lkgy3judc40lnxbo.lambda-url.us-east-1.on.aws/?key=%(name)s_%(time)s')
