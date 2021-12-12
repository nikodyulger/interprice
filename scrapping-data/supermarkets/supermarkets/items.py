import scrapy

class CarrefourPromoItem(scrapy.Item):
    name= scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
