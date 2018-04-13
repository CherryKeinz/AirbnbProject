# coding=utf-8
#!/usr/bin/env python
import requests
import codecs
URL = 'https://www.airbnb.com/rooms/3849435'
TXTFILE = 'detail.txt'

    # sid=NsT0d6RtpJ7WuVwwRzGZPIt0xQgp-4zwTuqqtMqO;
def spider():
    session =  requests.session()
    re = session.get(URL) # .content.decode("utf8","ignore").encode("gbk","ignore")
    with codecs.open(TXTFILE,'w',encoding='utf-8') as f:
        f.write(re.text)

    #return html.xpath('//a[@class="soldImg"]/img[@data_equip_name]')
spider()
