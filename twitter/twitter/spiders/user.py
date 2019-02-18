# -*- coding: utf-8 -*-
from scrapy import Request,Spider,cmdline,Selector
from twitter.items import TwitterUserItem
from urllib.parse import urlencode
import json

class UserSpider(Spider):
    name = 'user'
    allowed_domains = ['twitter.com']
    start_urls = ['https://twitter.com/TheWoodWalker/following']
    # 请查看浏览器在请求信息中将cookies信息复制到这里
    cookies_string = ''
    # 请查看浏览器第一个发出请求返回的min_position字段 针对于某个用户来说是固定的
    init_max_position = "1495539493925496309"
    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'referer': 'https://twitter.com/TheWoodWalker/following',
        }
    } 

    def __init__(self):
        cookies ={}
        for line in self.cookies_string.split(';'):
            key,value = line.split('=',1)
            cookies[key] = value
        self.cookies = cookies
     

    def page_page(self,max_position):
        data = {
            "include_available_features": '1',
            "include_entities": '1',
            "max_position": max_position,
            "reset_error_state": 'false',
        }
        params = urlencode(data)
        url = 'https://twitter.com/TheWoodWalker/following/users?' + params
        return Request(url, cookies=self.cookies, callback=self.parse_more)

    def start_requests(self):
        yield Request('https://twitter.com/TheWoodWalker/following', cookies=self.cookies, callback=self.parse)
        yield self.page_page(self.init_max_position)
        
    def parse(self, response):
        lis = response.css('.Grid-cell')
        for item in lis:
            userItem = TwitterUserItem()
            userItem['name'] = item.css('.fullname::text').extract_first()
            userItem['acccount_name'] = item.css('.ProfileCard-screenname .u-linkComplex-target::text').extract_first()
            userItem['desc'] = item.css('.ProfileCard-bio').xpath('string(.)').extract_first()
            yield userItem

    def parse_more(self, response):
        res =  json.loads(response.text)
        has_more_items = res['has_more_items']
        min_position = res['min_position'] 

        selector = Selector(text=res['items_html'], type="html")
        lis = selector.css('.Grid-cell')
        for item in lis:
            userItem = TwitterUserItem()
            userItem['name'] = item.css('.fullname::text').extract_first()
            userItem['acccount_name'] = item.css('.ProfileCard-screenname .u-linkComplex-target::text').extract_first()
            userItem['desc'] = item.css('.ProfileCard-bio').xpath('string(.)').extract_first()
            yield userItem

        if has_more_items:
            yield self.page_page(min_position)


if __name__ == '__main__':
    cmdline.execute("scrapy crawl user".split())