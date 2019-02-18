# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.exceptions import DropItem

class TwitterPipeline(object):
    def process_item(self, item, spider):
        if item['name']:
            item['name'] = item['name'].strip()
            return item
        else:
            raise DropItem("Item is empty")

class MongoPipeline(object):

    def __init__(self, mongo_url, mongo_db):
        print('__init__')
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        print('from_crawler')
        return cls(
            mongo_url = crawler.settings.get('MONGO_URL'),
            mongo_db = crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        print('open_spider')
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        name = item.__class__.__name__
        if self.db[name].update({'name': dict(item)['name']},{'$set': dict(item)}, True):
            print('保存成功')
        return item

    def close_spider(self, spider):
        print('close_spider')
        self.client.close()
