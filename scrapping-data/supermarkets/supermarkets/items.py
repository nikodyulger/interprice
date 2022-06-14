from scrapy import Item, Field

class ProductItem(Item):
    product_id = Field()
    supermarket = Field()
    name= Field()
    category = Field()
    subcategory = Field()
    price = Field()
    price_per_unit = Field()
    net_qty = Field()
    ingredients = Field()
    storage = Field()
    preparation = Field()
    manufacturer = Field()
    image_urls = Field()
    images = Field()
    last_updated=Field(serializer=str)
