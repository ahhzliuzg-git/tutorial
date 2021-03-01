import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
import time
import random
from tutorial.items import TutorialItem
from prepare_urls import yieldpage
# 进行分类分层级下载，注意 各级yield 参考https://zhuanlan.zhihu.com/p/58611444

# 进行分类分层级下载，注意 各级yield 参考https://zhuanlan.zhihu.com/p/58611444
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    pagenum=0

    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0'
      #   'SOME_SETTING': 'some value',
    }

           
    def start_requests(self):
# search result page list ,about ten thounds page
        start = time.time()
#get the total page


#        while self.pagenum<1:
#            time.sleep(random.uniform(1.1,2.4))
        for url1  in yieldpage(2):
                time.sleep(random.uniform(1.1,2.4))
                yield scrapy.Request(url=url1, callback=self.parse2)                   

        # while 1:
        #     try:
        #             #print(next(test1))
        #         time.sleep(random.uniform(1.1,2.4))
        #         url1=next(test1)
        #         yield scrapy.Request(url=url1, callback=self.parse2)                   
        #     except StopIteration:
        #             break

        end = time.time()
        self.log("运行时间:%.2f秒"%(end-start))
    def parse2(self,response):
            le=LinkExtractor(restrict_xpaths='///html/body/div[5]/div[2]/div/div/div[1]/ul',deny='/index.html$')
            for link in le.extract_links(response):
                time.sleep(random.uniform(1.1,5.4))
                yield Request(link.url,callback=self.parse_link)

    def parse_link(self,response):
        
        page=time.time().__str__()
        filename = 'html/quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
          #后续保存本级response页面的list
        #yield self.file_down(response)
        filedown= self.callmefordebug(response)
        for f in filedown:
            yield f
        
        #self.file_down1(response)
    def callmefordebug(self,response):
            self.log('call me')
            x=response.xpath('//a[@class="bizDownload"]')

            if x:
                #x1=x.xpath('./text()').extract()
                
                #x1=''.join(x)
                filen=response.xpath('//a[@class="bizDownload"]/text()').extract()
                filen=''.join(filen)
                self.log('---***---download file ： %s***---s' % filen)
                file=TutorialItem() #here hook to filepipleline lzg
                for lu in x:       
                    filen=lu.xpath('//a[@class="bizDownload"]/text()').extract()[0]
                    #x=''.join(x)
                    #filen=''.join(filen)
                    urlid=lu.xpath('//a[@class="bizDownload"]/@id').extract()[0]
                    self.log('*****download file urlid %s' % urlid)
                    url='http://www.ccgp.gov.cn/oss/download?uuid='+urlid
                    #file=TutorialItem() #here hook to filepipleline lzg
                    #first get the outline part file href
                    file['file_urls']=[url]
                    file['file_name']=filen
                    #file[name]=filen
                    self.log('*****download file Saved file %s' % filen)
                    yield  file

    def parsenum(self,response):
        res=response.xpath('/html/body/div[5]/div[1]/div/p[2]/script/text()')
        self.pagenum=res.re(r'size: (\d+)')[0]
        self.log('pagenun:%s'%self.pagenum)
        yield 1
#next we will 
