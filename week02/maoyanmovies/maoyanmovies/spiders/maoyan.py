# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from maoyanmovies.items import MaoyanmoviesItem


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        cookies = 'uuid_n_v=v1; uuid=73A84670B86F11EA909D9FF2C00A78C336F381410B1A45AD8F31F1947DC1123D; _lxsdk_cuid=172f5b16192c8-0a6f7139fdfbd9-4353760-144000-172f5b161921b; _lxsdk=73A84670B86F11EA909D9FF2C00A78C336F381410B1A45AD8F31F1947DC1123D; mojo-uuid=cd6b033fba6d946724b7d14876a0f1c6; _csrf=198ed6c294e96c7110b8604cb6c715d35f08c78f10d5ea5840123a2e3a749acb; mojo-session-id={"id":"50cfebd763c40b4e6a98b1080062a276","time":1593958996355}; mojo-trace-id=1; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593314713,1593352418,1593955200,1593958996; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593958996; __mta=174504477.1593259942553.1593955236701.1593958996600.13; _lxsdk_s=1731f5c19c5-cc8-4ef-157%7C%7C2'
        yield scrapy.Request(url, callback=self.parse, cookies=cookies, dont_filter=True)

    def parse(self, response):
        try:
            movies = Selector(response=response).xpath('//dd')
            for movie in movies[0:10]:
                title = movie.xpath('./div[1]/div[2]/a/div/div[1]/span[1]/text()')
                movieType = movie.xpath('./div[1]/div[2]/a/div/div[2]/text()')
                releaseTime = movie.xpath('./div[1]/div[2]/a/div/div[4]/text()')
                title = title.extract()[0]
                movieType = movieType.extract()[1].strip()
                releaseTime = releaseTime.extract()[1].strip()
                item = MaoyanmoviesItem()
                item['title'] = title
                item['movieType'] = movieType
                item['releaseTime'] = releaseTime
                print('------------')
                print(item)
                yield item
        except Exception as e:
            print(e)
            item = MaoyanmoviesItem()
            item['title'] = None
            item['movieType'] = None
            item['releaseTime'] = None
            yield item
