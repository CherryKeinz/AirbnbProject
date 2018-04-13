# -*- coding: utf-8 -*-
#!/usr/bin/env python
import requests
import cookielib
import urllib2
import codecs
import threading
import sys
import time
import base64
reload(sys)
sys.setdefaultencoding('utf-8')
from requests.auth import HTTPProxyAuth

# https://www.airbnb.com/rooms/747656
header = { 
'User-Agent' : 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
 }
proxie = {
	'https':'http://61.160.212.181:808',
	'https':'https://110.73.11.190:8123'
}
proxy_host = "proxy.crawlera.com"
proxy_port = "8010"
proxy_auth = "ac9bf1a504004538b4c6c7a561f5f14f:" # Make sure to include ':' at the end
proxies = {"https": "https://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port),
      "http": "http://{}@{}:{}/".format(proxy_auth, proxy_host, proxy_port)}
headers = {
   # other headers ...
   "Proxy-Authorization": 'Basic ' + base64.b64encode(proxy_auth)
}



def getURL(urlStart,urlEnd):
    with codecs.open('url/urlFrom'+ str(urlStart) +'.txt','w',encoding='utf-8') as f:
		for i in xrange(urlStart,urlEnd):
			url= 'https://www.airbnb.com/rooms/' + str(i)
			time.sleep(3)
			try:
				# s = requests.session()
				r = requests.get(url, proxies=proxies,allow_redirects=False,verify=False)
				print r.status_code
				if r.status_code == 200:
					print r.status_code
					print url
					f.write(url + '\n')
			except:
				print("Connection refused by the server..")
				print("Let me sleep for 5 seconds")
				print("ZZzzzz...")
				time.sleep(5)
				print("Was a nice sleep, now let me continue...")
				continue
def threadGet():
	urlStart = 1
	for i in xrange(5):
		urlEnd = urlStart + 500
		# t = threading.Thread(target=getURL,args=(urlStart,urlEnd))
		# t.start()
		getURL(urlStart,urlEnd)
		urlStart = urlEnd


threadGet()
