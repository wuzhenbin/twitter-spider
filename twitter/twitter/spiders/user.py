# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class UserSpider(scrapy.Spider):
    name = 'user'
    allowed_domains = ['twitter.com']
    base_url = 'https://twitter.com/TheWoodWalker/following'

    def start_requests(self):
        yield SplashRequest(
            url=self.base_url, 
            callback=self.parse, 
            endpoint='render.html',
            args={
                'proxy': 'http://172.16.23.228:1080',
            }
        )

    def parse(self, response):
        lis = response.css('.js-stream-item .Grid-cell')
        for item in lis: 
            title = item.css('a.fullname::text').extract_first()
            print(title,'title')
