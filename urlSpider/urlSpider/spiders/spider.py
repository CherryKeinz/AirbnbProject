#-*- coding: utf-8 -*-
import scrapy
from urlSpider.items import UrlspiderItem
import sys
import pandas as pd
import time
from scrapy.http import Request
reload(sys)
sys.setdefaultencoding("utf-8")
FILE_SIZE = 50

class spriderDemo(scrapy.spiders.Spider):
    # -name: 用于区别Spider。 该名字必须是唯一的，您不可以为不同的Spider设定相同的名字。
    # 命令行中 scrapy crawl + name
    name = "spider"
    custom_settings = {
        'ITEM_PIPELINES': {
            # settings.py中BOT_NAME的名字..pipelines.JsonWithEncodingPipeline
            'urlSpider.pipelines.UrlspiderPipeline': 100,  # 开通CrawlerStorePipeline
        },
    }
    # _v72lrv
    def start_requests(self):
        df = pd.read_csv('Neighborhood.csv').drop_duplicates()
        df.fillna(0, inplace=True)
        for indexs in df.index:
            if df.loc[indexs].values[0] is 0:
                df.loc[indexs].values[0] = df.loc[indexs].values[1] + df.loc[indexs].values[2]
            else:
                df.loc[indexs].values[0] += df.loc[indexs].values[1] + df.loc[indexs].values[2]
        arrs =  df.iloc[:, 0]
        group = 1
        for index,cityName in enumerate(arrs):
            start_urls = []
            url = 'https://www.airbnb.com/s/'+ cityName\
                  +'/homes?refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&locale=en&s_tag=3qZONWvv&cdn_cn=1'
            start_urls.append(url)
            if index > FILE_SIZE * group:
                group += 1
            for i in xrange(17):
                start_urls.append(url + '&section_offset=' + str(i))
            for url in start_urls:
                yield Request(url=url,meta={'group': str(group)}, callback=self.parse)

    def parse(self, response):
        try:
            item = UrlspiderItem()
            item['group'] = response.meta['group']
            # s = requests.session()
            hostUrl = 'https://www.airbnb.com'
            if len(response.xpath('//div[@class="_v72lrv"]').extract()) is 0:
                return
            urlList = []
            for content in response.xpath('//div[@class="_v72lrv"]'):
                urlList.append(hostUrl + content.xpath('div/a/@href').extract()[0] + '\n')
            item['urlList'] = urlList
            return item
        except:
            print("Something wrong..")
            return