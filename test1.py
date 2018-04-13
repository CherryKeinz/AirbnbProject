# coding=utf-8
#!/usr/bin/env python
import requests
import json
from lxml import etree

import codecs 

#URL = "http://xyq.cbg.163.com/cgi-bin/query.py?act=query&server_id=402&areaid=12&server_name=%B2%B3%BA%A3%C3%F7%D6%E9&page=1&kindid=27&kind_depth=2"
#URL = 'http://xyq.cbg.163.com/cgi-bin/query.py?act=query'
# URL = 'http://xyq.cbg.163.com/cgi-bin/query.py?act=query&server_id=402&areaid=12&server_name=%B2%B3%BA%A3%C3%F7%D6%E9&page=1&kindid=0&kind_depth=1'
URL = 'http://res.xyq.cbg.163.com/js/server_list_data.js'
TXTFILE = 'content.txt'
COOKIE = '_ntes_nnid=3268a9c15ae861662ac5ef15858f38d4,1515305795958;\
 _ntes_nuid=3268a9c15ae861662ac5ef15858f38d4; vjuids=a277a813e.160d05796c6.0.8bfc328c9fe5d;\
  usertrack=ezq0pVpSAvSAQvDkdg0ZAg==; \
  vinfo_n_f_l_n3=2519af5ccd7047b8.1.1.1515324145885.1515324891896.1515326840644; \
  vjlast=1515323889.1516431473.13; \
  last_login_serverid=402'
    # sid=NsT0d6RtpJ7WuVwwRzGZPIt0xQgp-4zwTuqqtMqO;
def spider():
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'Cookie':COOKIE,
        'Host':'xyq.cbg.163.com',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}

    # resp = requests.get(url=URL)
    # print (resp.text)
    # print ('resp', resp.cookies)
    # print ('req', resp.request._cookies)
    session =  requests.session()



    re = session.get(URL,headers = headers) # .content.decode("utf8","ignore").encode("gbk","ignore")
    html = etree.HTML(re.text)
    with codecs.open(TXTFILE,'w',encoding='utf-8') as f:
        f.write(re.text)

    return html.xpath('//a[@class="soldImg"]/img[@data_equip_name]')
spider()
