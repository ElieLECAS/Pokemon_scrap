# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PokeScrapItem(scrapy.Item):
    name = scrapy.Field()    
    price = scrapy.Field()
    description = scrapy.Field()
    stock = scrapy.Field()
    sku = scrapy.Field()
    categories = scrapy.Field()
    tags = scrapy.Field()
    weight = scrapy.Field()
    height = scrapy.Field()
    length = scrapy.Field()
    width = scrapy.Field()

