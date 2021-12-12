import scrapy

class SupermarketsItem(scrapy.Item):
    name= scrapy.Field()
    price = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
