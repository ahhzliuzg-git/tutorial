import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
import time
import random
from tutorial.items import TutorialItem
from prepare_urls import yieldpage

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0'
      #   'SOME_SETTING': 'some value',
    }
    def start_requests1(self):
        urls = [
'http://search.ccgp.gov.cn/bxsearch?searchtype=2&page_index=100&bidSort=0&buyerName=&projectId=&pinMu=0&bidType=0&dbselect=bidx&kw=&start_time=2019%3A02%3A13&end_time=2019%3A08%3A14&timeType=5&displayZone=&zoneId=&pppStatus=0&agentName='
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def start_requests(self):
# search result page list ,about ten thounds page
            test1=yieldpage(10)

            while True:
                try:
                    #print(next(test1))
                    time.sleep(random.uniform(1.1,5.4))
                    url1=next(test1)
                    yield scrapy.Request(url=url1, callback=self.parse)
                   
                except StopIteration:
                    break 

    def parse(self, response):
#in  each  search result page ,we get down it's content with file form,and downlaod file attachment .
        le=LinkExtractor(restrict_xpaths='///html/body/div[5]/div[2]/div/div/div[1]/ul',deny='/index.html$')
        for link in le.extract_links(response):
            time.sleep(random.uniform(1.1,5.4))
            yield Request(link.url,callback=self.parse_link)
       #后续保存本级response页面的list

    def parse_link(self,response):
        
        page=time.time().__str__()
        filename = 'html/quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
          #后续保存本级response页面的list
        #self.file_down(response)

    #def file_down(self,response): /div[2]/div/div[2]/div/div[2]/table/tbody/
       # le=LinkExtractor(restrict_xpaths='//*[@id="//*[@id="detail"]/div[2]/div/div[2]/div/div[2]/table/tbody',deny='/index.html$')
        x=response.xpath('//a[@class="bizDownload"]/@id').extract()
        if x:
            filen=response.xpath('//a[@class="bizDownload"]/text()').extract()
            x=''.join(x)
            filen=''.join(filen)
            url='http://www.ccgp.gov.cn/oss/download?uuid='+x

            file=TutorialItem() #here hook to filepipleline lzg
            #first get the outline part file href
            file['file_urls']=[url]
            file['file_name'] =filen
            #file[name]=filen
            self.log('*****download file Saved file %s' % filen)
           # yield file
            return file
       