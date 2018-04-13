# -*- coding: utf-8 -*-
#!/usr/bin/env python
import requests
import json
from lxml import etree
import cookielib
import urllib2
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

URL = "http://xyq.cbg.163.com/cgi-bin/query.py?act=query&server_id=402&areaid=12&server_name=%B2%B3%BA%A3%C3%F7%D6%E9&page=1&kindid=27&kind_depth=2"


def test():
    url = 'https://www.airbnb.com/api/v2/explore_tabs?version=1.3.5&_format=for_explore_search_web&experiences_per_grid=20&items_per_grid=18&guidebooks_per_grid=20&auto_ib=false&fetch_filters=true&has_zero_guest_treatment=false&is_guided_search=true&is_new_cards_experiment=true&luxury_pre_launch=false&query_understanding_enabled=true&show_groupings=true&supports_for_you_v3=true&timezone_offset=480&metadata_only=false&is_standard_search=true&tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&s_tag=mbEt07y-&section_offset=2&last_search_session_id=76d241ef-1ee6-4efc-8dce-54e75f793d6a&federated_search_session_id=28742439-884b-437b-b80f-35dbdc87cb70&screen_size=small&_intents=p1&key=d306zoyjsyarp7ifhu67rjxn52tv0t20&currency=CNY&locale=en'
    r = requests.get(url)
    with codecs.open('tset1.json','w',encoding='utf-8')as f:
        f.write(r.content)

img = test()


