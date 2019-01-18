# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

class YingjiesPipeline(object):
    def process_item(self, item, spider):
        job = []
        for i in item['job']:
            if i.strip() != '':
                job.append(i.strip())
        item['job'] = ''.join(job)
        return item

class MongoPipeline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(settings['MONGOHOST'], settings['MONGOPORT'])
        db = self.client[settings['MONGODB']]
        self.collection = db[settings['COLLECTION']]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
