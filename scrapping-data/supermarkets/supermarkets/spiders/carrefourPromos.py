import scrapy
from scrapy_playwright.page import PageCoroutine
from ..items import CarrefourPromoItem

class carrefourPromosSpider(scrapy.Spider):
    name = 'carrefourPromos'
    start_urls = [
        'https://www.carrefour.es/supermercado/el-mercado-promocion/F-10flZ1023/c']
    r_meta = dict(
        playwright=True,
        playwright_include_page=True,
        playwright_page_coroutines=[
            PageCoroutine(
                "press", selector="body", key="PageDown"),
            PageCoroutine(
                "wait_for_selector", "img[lazy='loaded']"),
            PageCoroutine(
                "press", selector="body", key="PageUp"),
            PageCoroutine("wait_for_timeout", 3000),
            PageCoroutine(
                "press", selector="body", key="PageDown"),
            # PageCoroutine("wait_for_timeout", 3000),
            # PageCoroutine(
            #     "screenshot", path="screenshot.png", full_page=True)
        ]
    )

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0],
                             callback=self.parse,
                             meta=self.r_meta)

    async def parse(self, response):
        promos = response.css(
            "li.product-card-list__item div[data-origin='list']")

        for promo in promos:
            name = promo.css(
                'a.product-card__title-link::text').get().strip()
            price = promo.css('span.product-card__price::text').get()

            if price == None:
                price = promo.css(
                    'span.product-card__price--current::text').get().strip()
            else:
                price = price.strip()

            url_img = promo.css(
                'img.product-card__image::attr(src)').get()

            yield CarrefourPromoItem(name=name, price=price, image_urls=[url_img])
