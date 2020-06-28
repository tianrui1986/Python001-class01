# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pandas as pd


class MaoyanmoviePipeline:
    # def process_item(self, item, spider):
    #     return item

    # 将获取到的数据存入csv文件
    def process_item(self, item, spider):
        title = item['title']
        movieType = item['movieType']
        releaseTime = item['releaseTime']
        data_list = [title, movieType, releaseTime]
        # 将获取的数据存入CSV文件
        movies = pd.DataFrame(data=[data_list])
        movies.to_csv('../movies.csv', encoding='utf-8', index=False, header=False, mode='a')
        return item