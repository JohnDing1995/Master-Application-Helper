# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class OnepointthreeacresscarpingPipeline(object):
    def process_item(self, item, spider):
        file = open("ad_information.txt", "a")
        item_string = str(item).decode("unicode_escape").encode('utf-8')
        file.write(item_string)
        file.write('\n')
        file.close()
        #print(item_string)
        return item
