# -*- coding: utf-8 -*-
import scrapy
import json

class UsernameSpider(scrapy.Spider):
    name = 'username'
    allowed_domains = ['www.stocktwits.com']
    start_urls = ['https://api.stocktwits.com/api/2/streams/symbol/AAPL.json?filter=top']

    def parse(self, response):
        print('...............................', json.loads(response.body)['response'])
