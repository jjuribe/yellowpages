# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YellowpagesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class JItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    phone = scrapy.Field()
    website = scrapy.Field()
    logo = scrapy.Field()
    email = scrapy.Field()
    image = scrapy.Field()

    pass
