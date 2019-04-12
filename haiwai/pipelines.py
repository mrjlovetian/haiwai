# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class HaiwaiPipeline(object):
    def process_item(self, item, spider):
        db = pymysql.connect('localhost', 'root', '897011805', 'yhj')
        cursor = db.cursor()
        symbol = pymysql.escape_string(item['symbol'])
        title = pymysql.escape_string(item['title'])
        watchlist_count = item['watchlist_count']
        pinglun = pymysql.escape_string(item['pinglun'])
        created_at = pymysql.escape_string(item['created_at'])
        sourcetitle = pymysql.escape_string(item['sourcetitle'])
        username = pymysql.escape_string(item['username'])
        followers = item['followers']
        following = item['following']
        join_date = pymysql.escape_string(item['join_date'])
        name = pymysql.escape_string(item['name'])
        watchlist_stocks_count = item['watchlist_stocks_count']
        sql = """INSERT INTO haiwai values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""%(symbol, title, watchlist_count, pinglun, created_at, sourcetitle, username, followers, following, join_date, name, watchlist_stocks_count)
        cursor.execute(sql)
        db.commit()
        db.close()
        return item
        return item
