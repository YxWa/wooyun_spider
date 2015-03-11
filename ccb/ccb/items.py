# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
#
#
# class CcbItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass
#

import scrapy

class CcbItem(scrapy.Item):
    #number = scrapy.Field()
    title = scrapy.Field()
    submit_time = scrapy.Field()
    level = scrapy.Field()
    #type = scrapy.Field()
    #level = scrapy.Field()