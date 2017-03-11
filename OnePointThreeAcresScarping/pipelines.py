# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymongo

class OnepointthreeacresscarpingPipeline(object):

    def __init__(self):
        self.file = open('admission_information.jl','wb')

    def process_item(self, item, spider):
        line = json.dumps(item) + "\n"
        self.file.write(line)
        return item

class MongoDBPipeline(object)

    def __init__(self):
        self.mongo_url = "localhost"
        self.mongo_db = "one_point_three_acres"

    def 