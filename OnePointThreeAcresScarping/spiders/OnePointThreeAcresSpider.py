from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.spider import Spider, Request
from OnePointThreeAcresScarping.items import AdmissionInformation

class OnePointThreeAcresSpider(Spider):
    name = "ad_information"
    allowed_domains = ["1point3acres.com"]
    start_url = "http://www.1point3acres.com/bbs/forum-82-1.html"


    def get_next_url(self,oldurl):
        l = oldurl.split('-')
        pagenumber = int(l[2].split('.')[0])
        newnumber = pagenumber+1
        if newnumber <=500:
            nexturl = l[0] + "-" + l[1] + "-" + str(newnumber) + ".html"
            return str(nexturl)
        else:
            return
    def start_requests(self):
        yield Request(self.start_url)

    def request_page(self,start_url):
        url = start_url
        while url != None:
            yield Request(url,self.parse)
            url = self.get_next_page(url)

    def parse(self,response):
        pageinformation = response.xpath('//*[@id="threadlisttableid"]')
        for eachstudent in pageinformation:
            item = AdmissionInformation()
            item['admission_time'] = response.xpath('//*[contains(@id, "normalthread")]/tr/th/span/font[1]/text()').extract()
            item['gre'] = response.xpath('//*[contains(@id, "normalthread")]/tr/th/span/font[3]/text()').extract()
            item['gpa'] = response.xpath('//*[contains(@id, "normalthread")]/tr/th/span/font[5]/text()').extract()
            item['undergrad_school'] = response.xpath('//*[contains(@id, "normalthread")]/tr/th/span/font[6]/text()').extract()
            item['major'] = response.xpath('//*[contains(@id, "normalthread")]/tr/th/span/font[4]/text()').extract()
            item['english_grade'] = response.xpath('//*[contains(@id, "normalthread")]/tr/th/span/font[2]/text()').extract()
            item['year'] = response.xpath('//*[contains(@id, "normalthread")]/tr/th/span/u/font[1]/text()').extract()
            item['admission_type'] = response.xpath('//*[contains(@id, "normalthread")]/tr/th/span/u/font[2]/text()').extract()
            item['admission_school'] = response.xpath('//*[contains(@id, "normalthread")]/tr/th/span/u/font[5]/text()').extract()
            item['admission_major'] = response.xpath('//*[contains(@id,"normalthread")]/tr/th/span/u/font[4]/b/text()').extract()
            item['title'] = response.xpath('//*[contains(@id,"normalthread")]/tr/th/a[2]/text()').extract()
            yield item
        next_url = self.get_next_url(response.url)
        if next_url != None:
            yield Request(next_url)




    # //*[ @ id = "normalthread_244396"]