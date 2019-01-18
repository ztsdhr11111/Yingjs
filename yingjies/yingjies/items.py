# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pub_date = scrapy.Field()
    workplace = scrapy.Field()
    position = scrapy.Field()
    position_type = scrapy.Field()
    job = scrapy.Field()