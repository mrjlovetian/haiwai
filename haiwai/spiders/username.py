# -*- coding: utf-8 -*-
import scrapy
import json

class UsernameSpider(scrapy.Spider):
    name = 'username'
    allowed_domains = ['www.stocktwits.com']
    start_urls = ['https://api.stocktwits.com/api/2/streams/symbol/AAPL.json?filter=top']

    def parse(self, response):
        body = json.loads(response.body)
        maxstr = body['cursor']['max']
        symbol = body['symbol']['symbol']
        title = body['symbol']['title']
        watchlist_count = body['symbol']['watchlist_count']
        for message in body['messages']:
            body = message['body']
            created_at = message['created_at']
            sourcetitle = message['source']['title']
            # symbols = ''
            # for symbol in message['symbols'][0]:
            #     symbols = symbol[''] + ',' 
            username = message['user']['username']
            followers = message['user']['followers']
            following = message['user']['following']
            join_date = message['user']['join_date']
            name = message['user']['name']
            watchlist_stocks_count = message['user']['watchlist_stocks_count']
            print('..........', username, body, sourcetitle, join_date)


        
