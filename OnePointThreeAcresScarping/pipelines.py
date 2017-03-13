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
        item_db = dict(item)
        #print(item_db)
        each_record = {}
        print(type(item_db.items()))

        print(len(item_db['year']))

        for i in range(0,len(item_db['year'])-1):
            each_record = item_db.copy()
            for key,each_v in item_db.items():

            #print(type(v))
            #for k,each_v in v:
                each_record[key] = each_v[i]
                #print(each_v[i])
            #print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            #print(each_record)
            self.collection.save(each_record)
        # each_record = {single[0]:single[1][i]}
        #
        log.msg('Admission information added to the database',level=log.DEBUG,spider=spider)
        return item
