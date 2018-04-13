# coding=utf-8
#!/usr/bin/env python
import requests
import json
from lxml import etree

import codecs 

#URL = "http://xyq.cbg.163.com/cgi-bin/query.py?act=query&server_id=402&areaid=12&server_name=%B2%B3%BA%A3%C3%F7%D6%E9&page=1&kindid=27&kind_depth=2"
#URL = 'http://xyq.cbg.163.com/cgi-bin/query.py?act=query'
# URL = 'http://xyq.cbg.163.com/cgi-bin/query.py?act=query&server_id=402&areaid=12&server_name=%B2%B3%BA%A3%C3%F7%D6%E9&page=1&kindid=0&kind_depth=1'
URL = 'https://www.airbnb.com/api/v2/explore_tabs?version=1.3.5&_format=for_explore_search_web&experiences_per_grid=20&items_per_grid=18&guidebooks_per_grid=20&auto_ib=false&fetch_filters=true&has_zero_guest_treatment=false&is_guided_search=true&is_new_cards_experiment=true&luxury_pre_launch=false&query_understanding_enabled=true&show_groupings=true&supports_for_you_v3=true&timezone_offset=480&metadata_only=false&is_standard_search=true&tab_id=home_tab&section_offset=6&items_offset=54&recommendation_item_cursor=&refinement_paths%5B%5D=%2Fhomes&place_id=&title_type=MAGAZINE_HOMES&allow_override%5B%5D=&s_tag=TnCqU_qN&last_search_session_id=dea59f16-7267-4dbc-90a6-bf2298252599&federated_search_session_id=d3a971fc-1df8-4e06-8aba-afe8c3138268&screen_size=small&_intents=p1&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=CNY&locale=en'
TXTFILE = 'content.txt'

    # sid=NsT0d6RtpJ7WuVwwRzGZPIt0xQgp-4zwTuqqtMqO;
def spider():
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Cache-Control':'max-age=0',
        'Connection':'keep-alive',
        'referer':'https://www.airbnb.com/s/homes?refinement_paths%5B%5D=%2Fhomes&place_id=&query=&title_type=MAGAZINE_HOMES&allow_override%5B%5D=&s_tag=TnCqU_qN',
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

    #return html.xpath('//a[@class="soldImg"]/img[@data_equip_name]')
spider()
