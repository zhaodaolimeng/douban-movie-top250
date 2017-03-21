# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name_cn = scrapy.Field()
    name_en = scrapy.Field()
    name_other = scrapy.Field()
    director_actor = scrapy.Field()
    year = scrapy.Field()
    country = scrapy.Field()
    types = scrapy.Field()
    comment = scrapy.Field()
    pass
