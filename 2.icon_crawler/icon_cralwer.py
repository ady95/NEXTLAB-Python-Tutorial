# -*- coding:utf-8 -*-

import os, sys
import urllib
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('utf-8')

URL = "https://www.iconfinder.com/search/?q=%s"

def crawlImage(keyword):
	count = 0
	url = URL % keyword
	
	response = urllib.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html)
	#print soup.prettify()
	
	#http://coreapython.hosting.paran.com/etc/beautifulsoup4.html#css-selectors
	icons = soup.select(".tiled-icon")
	if len(icons) == 0:
		print "아이콘을 찾을 수 없습니다"
	else:
		print icons

	for icon in icons:
		count += 1
		img_src = icon["src"]
		filename, fileExt = os.path.splitext(img_src)
		print img_src
			
if __name__ == '__main__':
	crawlImage("computer")	
