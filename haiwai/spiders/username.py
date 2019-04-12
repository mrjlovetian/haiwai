# -*- coding: utf-8 -*-
import scrapy
import json
from haiwai.items import HaiwaiItem

class UsernameSpider(scrapy.Spider):
    name = 'username'
    allowed_domains = ['stocktwits.com']
    baseUrl = 'https://api.stocktwits.com/api/2/streams/symbol/AAPL.json?filter=top'
    start_urls = [baseUrl]

    def parse(self, response):
        body = json.loads(response.body)
        maxstr = body['cursor']['max']
        symbol = body['symbol']['symbol']
        title = body['symbol']['title']
        watchlist_count = body['symbol']['watchlist_count']
        for message in body['messages']:
            item = HaiwaiItem()
            pinglun = message['body']
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
            item['symbol'] = symbol
            item['title'] = title
            item['watchlist_count'] = watchlist_count
            item['pinglun'] = pinglun
            item['created_at'] = created_at
            item['sourcetitle'] = sourcetitle
            item['username'] = username
            item['followers'] = followers
            item['following'] = following
            item['join_date'] = join_date
            item['name'] = name
            item['watchlist_stocks_count'] = watchlist_stocks_count
            yield item
            print('..........', username, pinglun, sourcetitle, join_date)

        url = self.baseUrl + '&max=' + str(maxstr)
        yield scrapy.Request(url=url, callback = self.parse)


        
