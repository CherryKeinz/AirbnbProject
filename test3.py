# -*- coding: utf-8 -*-
#!/usr/bin/env python
import requests
import json
from lxml import etree

import sys

reload(sys) 
sys.setdefaultencoding('utf8')
#URL = "http://xyq.cbg.163.com/cgi-bin/query.py?act=query&server_id=402&areaid=12&server_name=%B2%B3%BA%A3%C3%F7%D6%E9&page=1&kindid=27&kind_depth=2"
URL = 'http://xyq.cbg.163.com/cgi-bin/query.py?act=query'
TXTFILE = 'content.txt'


def spider():
    url="http://xyq.cbg.163.com/cgi-bin/query.py?act=query&server_id=402&areaid=12&server_name=%B2%B3%BA%A3%C3%F7%D6%E9&page=1&kindid=27&kind_depth=2"
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Host':'xyq.cbg.163.com',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    print '22'
##    session =  requests.session() 
##    session.get(URL)
    re = requests.post(URL,headers = headers)
    print re.text
    html = etree.HTML(re.text)
##    with open(TXTFILE,'w') as f:
##        f.write(re.text)
    print '11'
    return html.xpath('//a[@class="soldImg"]/img[@data_equip_name]')
spider()
