# -*- coding: utf-8 -*-
from scrapy import Request,Spider,cmdline

class UserSpider(Spider):
    name = 'user'
    allowed_domains = ['twitter.com']
    start_urls = ['https://twitter.com/TheWoodWalker/following']
    cookies = 'personalization_id="v1_+IFi/GRP+lNdtg8CelnzRA=="; guest_id=v1%3A154682759590985011; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _ga=GA1.2.627313887.1549964391; ads_prefs="HBERAAA="; kdt=ea4XihSoDAsPnrK9H8GRdCGk6NcpeYS3c2Nbostm; remember_checked_on=1; twid="u=989306118248611840"; auth_token=755079ef669d870ea20db0865fa9815ee7e1afe3; csrf_same_site_set=1; csrf_same_site=1; lang=zh-cn; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCD2jD%252FVoAToHaWQiJWI2%250AMzY2NzM2M2ZiNTNhZTM3ODlmNWIyMDhjOTAxMDliOgxjc3JmX2lkIiVhMDYx%250ANjc4Yjk4ZmYyZGEzNzYwZTM3OTgxYzJjYjAwOQ%253D%253D--e7eab9944510280c824f0e0992c68218d56f70ab; ct0=b0b2ff7b8a065d3cbb21ba3fc680e9d2; _gid=GA1.2.58967274.1550299673'

    custom_settings = {
        "DEFAULT_REQUEST_HEADERS": {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'referer': 'https://twitter.com/TheWoodWalker/following',
        }
    } 

    def start_requests(self):
        cookie ={}
        for line in self.cookies.split(';'):
            key,value = line.split('=',1)
            cookie[key] = value
        yield Request('https://twitter.com/TheWoodWalker/following', cookies=cookie)

    def parse(self, response):
        print(response)
        print(response.xpath('//head/title/text()').extract(),"777777777")
        lis = response.css('.GridTimeline')
        for item in lis:
            name = item.css('.fullname').extract_first()
            print(name,"&&&&&")


if __name__ == '__main__':
    cmdline.execute("scrapy crawl user".split())