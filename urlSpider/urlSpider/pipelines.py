# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs

class UrlspiderPipeline(object):
    # def __init__(self):
    def close_spider(self,spider):
        #关闭文件
        self.file.close()
    #最后也需要调用process_item返回item
    def process_item(self, item, spider):
        self.file = codecs.open('resultByGroup/' + item['group'] + '.txt', 'a+', encoding='utf-8')
        for i in item['urlList']:
            self.file.write(i)
        self.file.close()
        return item
