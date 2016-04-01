# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy import  log
from scrapy.exceptions import DropItem


class SjgtwCompanysPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient("mongodb://guanxiaoda.cn:27017")
        db = connection['sjgtwdb']
        self.collection = db['sjgtw_company']

        self.url_crawled = set()
        pipeline = [
            {
                "$group":{
                    "_id":"$url","count":{"$sum":1}
                }
            }
        ]
        result = list(self.collection.aggregate(pipeline))
        for i,item in enumerate(result):
            self.url_crawled.add(item['_id'])
            if i % 100 == 0 : print(i)
        log.msg("read %d crawled items" % len(result))

    def process_item(self, item, spider):
        valid = True
        # if item['name'] and item['model'] and item['price']:
        #     valid = True
        # else:
        #     valid = False
        #     DropItem('info not complete %s ' % item['name'])
        if not item['name']:
            valid = False
            DropItem('no name parsed.' )
        elif item['url'] in self.url_crawled:
            valid = False
            DropItem("item crawled before %s " % item['name'])
        else:
            valid = True

        if valid:
            self.collection.insert(dict(item))
            log.msg("item wrote to mongodb database %s/%s" % ('sjgtwdb', 'sjgtw_company'))
        return item
