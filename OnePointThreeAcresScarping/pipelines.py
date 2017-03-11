# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log

class OnepointthreeacresscarpingPipeline(object):

    def __init__(self):
        self.file = open('admission_information.jl','wb')

    def process_item(self, item, spider):
        line = json.dumps(item) + "\n"
        self.file.write(line)
        return item


class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings['MONGODB_SEVER'],
            settings['MONGODB_PORT']
        )
        db = connection.settings['MONGODB_DBNAME']
        self.collection =db[settings['MONGODB_COLLECTION']]


    def process_item(self,item, spider):
        vaild = True
        for data in item:
            if not data:
                vaild = False
                raise DropItem('Missing'.format(data))
            if vaild:
                self.collection.insert(dict(item))
                log.msg('Admission information added to the database',level=log.DEBUG,spider=spider)
        return item
