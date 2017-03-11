# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AdmissionInformation(scrapy.Item):

    # define the fields for your item here like:
    # name = scrapy.Field()
    undergrad_school = scrapy.Field()
    major = scrapy.Field()
    title = scrapy.Field()
    link = scrapy.Field()
    gpa = scrapy.Field()
    admission_school = scrapy.Field()
    admission_major = scrapy.Field()
    admission_year = scrapy.Field()
    admission_type = scrapy.Field() #MS or PhD
    english_grade = scrapy.Field()  #Toefl or Ielts
    gre = scrapy.Field()
    admission_time = scrapy.Field()
    year = scrapy.Field() #17fall,18Spring

    pass
