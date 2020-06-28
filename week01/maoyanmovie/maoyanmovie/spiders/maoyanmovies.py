# -*- coding: utf-8 -*-
import scrapy
from maoyanmovie.items import MaoyanmovieItem
from scrapy.selector import Selector


class MaoyanmoviesSpider(scrapy.Spider):
    name = 'maoyanmovies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass

    # 将url写入调度
    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)

    # 处理函数
    def parse(self, response):
        # print(response.url)
        movies = Selector(response=response).xpath('//dd')
        # print('++++++++++')
        # print(movies)
        for movie in movies[0:10]:
            title = movie.xpath('./div[1]/div[2]/a/div/div[1]/span[1]/text()')
            movieType = movie.xpath('./div[1]/div[2]/a/div/div[2]/text()')
            releaseTime = movie.xpath('./div[1]/div[2]/a/div/div[4]/text()')
            # print('--------------')
            # print(title)
            # print(movieType)
            # print(releaseTime)
            print('--------------')
            title = title.extract()[0]
            movieType = movieType.extract()[1].strip()
            releaseTime = releaseTime.extract()[1].strip()
            print(title)
            print(movieType)
            print(releaseTime)
            item = MaoyanmovieItem()
            item['title'] = title
            item['movieType'] = movieType
            item['releaseTime'] = releaseTime
            yield item
