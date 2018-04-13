# -*- coding: utf-8 -*-
#!/usr/bin/env python
import requests
import json
from lxml import etree
import cookielib
import urllib2
import codecs
import sys
import re
reload(sys)
sys.setdefaultencoding('utf-8')

URL = 'www.airbnb.com/api/v2/explore_tabs?version=1.3.5&_format=for_explore_search_web&experiences_per_grid=20&items_per_grid=18&guidebooks_per_grid=20&auto_ib=true&fetch_filters=true&has_zero_guest_treatment=false&is_guided_search=true&is_new_cards_experiment=true&luxury_pre_launch=false&query_understanding_enabled=true&show_groupings=true&supports_for_you_v3=true&timezone_offset=480&metadata_only=false&is_standard_search=true&tab_id=home_tab&section_offset=5&items_offset=72&recommendation_item_cursor=&refinement_paths%5B%5D=%2Fhomes&place_id=&title_type=MAGAZINE_HOMES&cdn_cn=1&allow_override%5B%5D=&collection_ids%5B%5D=1&s_tag=Ua3ajCaj&last_search_session_id=94a5d514-315e-4a10-8082-5a2a445f42dc&federated_search_session_id=a30c2ca2-f0c2-42af-b2bb-e374c7a5d15e&screen_size=medium&_intents=p1&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=CNY&locale=en'


def test():
        num = 50
        for i in range(1,20):
                url = 'http://www.airbnb.com/api/v2/explore_tabs?version=1.3.5&_format=for_explore_search_web&experiences_per_grid=20&items_per_grid='\
    		+ str(num) +'&guidebooks_per_grid=20&auto_ib=true&fetch_filters=true&has_zero_guest_treatment=false&is_guided_search=true&is_new_cards_experiment=true&luxury_pre_launch=false&query_understanding_enabled=true&show_groupings=true&supports_for_you_v3=true&timezone_offset=480&metadata_only=false&is_standard_search=true&tab_id=home_tab&section_offset='\
    		+str(i)+'&items_offset='+ str(i*num)+\
    		'&recommendation_item_cursor=&refinement_paths%5B%5D=%2Fhomes&place_id=&title_type=MAGAZINE_HOMES&cdn_cn=1&allow_override%5B%5D=&collection_ids%5B%5D=1&s_tag=Ua3ajCaj&last_search_session_id=94a5d514-315e-4a10-8082-5a2a445f42dc&federated_search_session_id=a30c2ca2-f0c2-42af-b2bb-e374c7a5d15e&screen_size=medium&_intents=p1&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=CNY&locale=en'
                r = requests.get(url)
                with codecs.open('test'+str(i)+'.json','w',encoding='utf-8')as f:
                        f.write(r.content)
def test2():
    url = 'https://www.airbnb.com/rooms/901882' + "?locale=en"
    idPattern = re.compile(r'\d+')
    print re.findall(idPattern,url)[0]
img = test2()


