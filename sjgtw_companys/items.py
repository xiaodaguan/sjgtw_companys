# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SjgtwCompanysItem(scrapy.Item):
    # define the fields for your item here like:
    brief = scrapy.Field()
    logo = scrapy.Field()
    banner = scrapy.Field()
    name = scrapy.Field()
    fund = scrapy.Field()
    scale = scrapy.Field()
    scope = scrapy.Field()
    cred = scrapy.Field()
    url = scrapy.Field()
    pass
