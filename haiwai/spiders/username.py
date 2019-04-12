# -*- coding: utf-8 -*-
import scrapy


class UsernameSpider(scrapy.Spider):
    name = 'username'
    allowed_domains = ['www.stocktwits.com']
    start_urls = ['http://www.stocktwits.com/']

    def parse(self, response):
        pass
