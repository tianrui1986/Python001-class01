# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class MaoyanmoviesPipeline:
    # def process_item(self, item, spider):
    #     return item

    def connect_mysql(self):
        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root123456',
                             db='scrapytest',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        return connection

    def process_item(self, item, spider):
        try:
            if item['title']:
                connection = self.connect_mysql()
                with connection.cursor() as cur:
                    sql = "Insert Into 'scrapyinfo' ('title', 'type', 'time') values(%s, %s, %s)"
                    cur.execute(sql, (item['title'], item['movieType'], item['releaseTime']))
                connection.commit()
        except Exception as e:
            print(e)
        finally:
            connection.close()
            return item
