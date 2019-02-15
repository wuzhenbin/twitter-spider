# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class UserSpider(scrapy.Spider):
    name = 'user'
    allowed_domains = ['twitter.com']
    # base_url = 'https://twitter.com/TheWoodWalker/following'
    base_url = 'http://www.google.com'

    def start_requests(self):
        yield SplashRequest(
            url=self.base_url, 
            callback=self.parse, 
            endpoint='render.html',
        )

    def parse(self, response):
    	print(response,"******")
        # lis = response.css('.js-stream-item .Grid-cell')
        # for item in lis: 
        #     title = item.css('a.fullname::text').extract_first()
        #     print(title,'title')
