# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# -*- coding: utf-8 -*-
from scrapy.pipelines.files import FilesPipeline
#from urlparse import urlparse
from os.path import basename,dirname,join
from urllib.parse import urlparse
# Define your item pipelines here
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.http import Request


class TutorialPipeline(FilesPipeline):

    def get_media_requests(self, item, info):
        #for file_url, file_name in zip(item['file_urls'], str(item['file_name'])):
            file_url=''.join(item['file_urls'])
            file_name=''.join(item['file_name'])
            yield Request(file_url, meta={'file_name': file_name})
            


    def file_path(self, request, response=None, info=None):
        #path=urlparse(request.url).path
      #  temp=join(basename(dirname(path)),basename(path))
      
        file_name = request.meta['file_name']
        #self.log('***file_path ： %s' % file_name)
        return 'src/%s' % ( file_name)