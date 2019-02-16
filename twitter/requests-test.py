import requests 
from requests.exceptions import RequestException
from pyquery import PyQuery as pq


headers = {
    'cookie': 'personalization_id="v1_+IFi/GRP+lNdtg8CelnzRA=="; guest_id=v1%3A154682759590985011; external_referer=padhuUp37zjgzgv1mFWxJ12Ozwit7owX|0|8e8t2xd8A2w%3D; _ga=GA1.2.627313887.1549964391; ads_prefs="HBERAAA="; kdt=ea4XihSoDAsPnrK9H8GRdCGk6NcpeYS3c2Nbostm; remember_checked_on=1; twid="u=989306118248611840"; auth_token=755079ef669d870ea20db0865fa9815ee7e1afe3; csrf_same_site_set=1; csrf_same_site=1; lang=zh-cn; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCD2jD%252FVoAToHaWQiJWI2%250AMzY2NzM2M2ZiNTNhZTM3ODlmNWIyMDhjOTAxMDliOgxjc3JmX2lkIiVhMDYx%250ANjc4Yjk4ZmYyZGEzNzYwZTM3OTgxYzJjYjAwOQ%253D%253D--e7eab9944510280c824f0e0992c68218d56f70ab; ct0=b0b2ff7b8a065d3cbb21ba3fc680e9d2; _gid=GA1.2.58967274.1550299673',
    'referer': 'https://twitter.com/TheWoodWalker/following',
}

win_proxies = {
    'http':  '127.0.0.1:1080',
    'https': '127.0.0.1:1080'
}

def get_response(url,params={},headers={},proxies={}):
    try:
        response = requests.get(url,params=params,headers=headers,proxies=proxies)
        if response.status_code == 200:
            return response.text
        return None 
    except RequestException as e:
        print('err: %s' % e)

html = get_response('https://twitter.com/TheWoodWalker/following',headers=headers,proxies=win_proxies)
# print(html)
header = pq(html).find('title').text()
print(header)
# header = doc('.GridTimeline .Grid-cell')
# lis = doc('.GridTimeline .Grid-cell')
# for item in lis:
#     name = pq(item).find('.fullname').text()
#     print(name)
