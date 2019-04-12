# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HaiwaiItem(scrapy.Item):
    maxstr = scrapy.Field()
    symbol = scrapy.Field()
    title = scrapy.Field()
    watchlist_count = scrapy.Field()
    pinglun = scrapy.Field()
    created_at = scrapy.Field()
    sourcetitle = scrapy.Field()
    username = scrapy.Field()
    followers = scrapy.Field()
    following = scrapy.Field()
    join_date = scrapy.Field()
    name = scrapy.Field()
    watchlist_stocks_count = scrapy.Field()
