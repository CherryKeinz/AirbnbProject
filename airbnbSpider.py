from selenium import webdriver
import codecs
import time
from bs4 import BeautifulSoup
URL ='https://www.airbnb.com/s/homes?refinement_paths%5B%5D=%2Fhomes&allow_override%5B%5D=&s_tag=pOsHCY9q&section_offset=18'
TXTFILE = 'content.txt'
browser = webdriver.Chrome(executable_path="D:/MyCode/Python/chromedriver.exe")
browser.get(URL)


##for i in range(10):
##    browser.execute_script("window.scrollTo(0,document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage")
##    time.sleep(3)
##    print(browser.page_source)
# 17556005    341978
# with codecs.open(TXTFILE,'w',encoding='utf-8') as f:
#     f.write(browser.page_source)

