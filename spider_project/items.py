# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join


class SpiderProjectItem(scrapy.Item):
    # define the fields for your item here:
    itemUrls = scrapy.Field()
    itemTitle = scrapy.Field()
    itemSummary = scrapy.Field()
    itemBasicInfo = scrapy.Field()
    itemCat = scrapy.Field()
    itemInfo = scrapy.Field()
    itemUpdateTime = scrapy.Field()
    itemReferance = scrapy.Field()
    itemTag = scrapy.Field()