# -*- coding: utf-8 -*-
from selenium import webdriver
import codecs
import time
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# demo.html就是主页面
def getUrl(content):
    soup = BeautifulSoup(content, "lxml")
    div = soup.find_all(attrs={'class': '_fhph4u'})
    urls = []
    s = set('')
    for i in div:
        for j in i.find_all('a'):
            # j['href']里面有重复的，我放到set里去重，然后再放到list
            url = "https://www.airbnb.com" + j['href']
            s.add(url)
    while len(s):
        urls.append(s.pop())
    return urls
def readCity():
    city = []
    with codecs.open('city.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            city.append(line.strip("\r\n"))
    return city

cities = readCity()
browser = webdriver.Chrome(executable_path="D:/MyCode/Python/chromedriver.exe")

city = 'Alaska'
for city in cities:
    urlTXT = 'url/'+city+'.txt'
    URL = 'https://www.airbnbchina.cn/s/'+city+'/homes?refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&s_tag=3qZONWvv'
    browser.get(URL)
# elem = browser.find_element_by_class_name("_1xxkdrug")
# elem.click()
# elem = browser.find_element_by_id("GeocompleteController-via-SearchBar")
# elem.send_keys(city)
    time.sleep(5)
    # 每一页
    with codecs.open(urlTXT,'w',encoding='utf-8') as f:
        for i in xrange(16):
            try:
                print('第' + str(i+1) + '页' )
                urls = getUrl(browser.page_source)
                for url_one in urls:
                    f.write(url_one)
                    f.write("\n")
                browser.find_element_by_class_name("_b8vexar").click()
                time.sleep(5)
            except:
                continue
# #实现屏幕的滚动
# for i in range(200):
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight); "
#                            "var lenOfPage=document.body.scrollHeight; return lenOfPage")
#     time.sleep(5)
#     print("第"+str(i)+"次下拉")



