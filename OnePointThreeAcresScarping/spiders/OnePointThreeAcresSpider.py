from scrapy.spiders import Spider
from scrapy.selector import Selector, HtmlXPathSelector
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
        if newnumber <= 1000:
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
        hxs = HtmlXPathSelector(response)
        march_re = r'">\s*(.*)\<'

        #for eachstudent in pageinformation:
        item = AdmissionInformation()
        item['admission_time'] = hxs.xpath('//*[contains(@id, "normalthread")]/tr/th/span/font[1]').re(r'">\s*(.*)\<')
        item['gre'] = hxs.xpath('//*[contains(@id, "normalthread")]/tr/th/span/font[3]').re(r': \s*(.*)\</font>')
        item['gpa'] = hxs.xpath('//*[contains(@id, "normalthread")]/tr/th/span/font[5]').re(r'">\s*(.*)\<')
        item['undergrad_school'] = hxs.xpath('//*[contains(@id, "normalthread")]/tr/th/span/font[6]').re(r'>(.*)\</font>')
        item['major'] = hxs.xpath('//*[contains(@id, "normalthread")]/tr/th/span/font[4]').re(r'color="green">\s*(.*)\<')
        item['english_grade'] = hxs.xpath('//*[contains(@id, "normalthread")]/tr/th/span/font[2]').re(r'>:\s*(.*)\<')
        item['year'] = hxs.xpath('//*[contains(@id, "normalthread")]/tr/th/span/u/font[1]').re(r'\[(.*)\<')
        item['admission_type'] = hxs.xpath('//*[contains(@id, "normalthread")]/tr/th/span/u/font[2]').re(r'">\s*(.*)\<')
        item['admission_school'] = hxs.xpath('//*[contains(@id, "normalthread")]/tr/th/span/u/font[5]').re(r'">\s*(.*)\<')
        item['admission_major'] = hxs.xpath('//*[contains(@id,"normalthread")]/tr/th/span/u/font[4]/b').re(r'<b>\s*(.*)\<')
        item['title'] = hxs.xpath('//*[contains(@id,"normalthread")]/tr/th/a[2]/text()').extract()

        links = hxs.xpath('//*[contains(@id,"normalthread")]/tr/th/a[2]').re(r'href\="([^\"]*)\"')
        urls_real = []
        for each in links:
            urls_real.append(each.replace('&amp;','&'))
            #print('url is:' + each.replace('&amp;','&'))
        item['link'] = urls_real



        yield item
        next_url = self.get_next_url(response.url)
        if next_url != None:
            yield Request(next_url)




    # //*[ @ id = "normalthread_244396"]