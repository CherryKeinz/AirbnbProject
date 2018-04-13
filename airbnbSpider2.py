# -*- coding: utf-8 -*-
from selenium import webdriver
import codecs
import time
from bs4 import BeautifulSoup
URL = 'https://www.airbnb.com'
TXTFILE = 'content.html'

# 进入浏览器设置
options = webdriver.ChromeOptions()
# 设置中文
options.add_argument('lang=en.UTF-8')
# 更换头部
options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
browser = webdriver.Chrome(executable_path="D:/MyCode/Python/chromedriver.exe",
                           chrome_options=options)


browser.get(URL)
time.sleep(3)
browser.find_element_by_class_name("_3uc7cf").click()
# _3uc7cf
# for link in links:
    # print link
for i in range(10):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage")
    time.sleep(3)

# 17556005    341978
with codecs.open(TXTFILE,'w',encoding='utf-8') as f:
    f.write(browser.page_source)

