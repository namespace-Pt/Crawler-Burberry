# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BurberryNewItem(scrapy.Item):
    # define the fields for your item here like:
    # image_urls = scrapy.Field()
    # image = scrapy.Field()
    price = scrapy.Field()
    name = scrapy.Field()