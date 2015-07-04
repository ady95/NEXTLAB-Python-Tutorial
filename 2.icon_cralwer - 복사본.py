# -*- coding:utf-8 -*-

import os, sys
from bs4 import BeautifulSoup
import mechanize
import urllib

reload(sys)
sys.setdefaultencoding('utf-8')

#KEYWORD = "setting+control"
#SAVE_FOLDER = r"D:\python\DATA\31"
URLs = ["https://www.iconfinder.com/search/?q=%s", "https://www.iconfinder.com/ajax/search/?page=%d&q=%s"]

def crawlImage(keyword):
	count = 0
	for i in range(0, 11):
		if i == 0:
			URL = URLs[0] % keyword
		else:
			URL = URLs[1] % (i, keyword)
	
		browser = mechanize.Browser()
		browser.set_handle_robots(False)
		response = browser.open(URL)
		html = response.read()
		soup = BeautifulSoup(html)
		#print soup.prettify()
		#sys.exit()
	
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
			#save_filename = "%d%s" % (count, fileExt)  
			#path = os.path.join(save_folder, save_filename)
			#print path
			# download image
			#urllib.urlretrieve(img_src, path)
			
if __name__ == '__main__':
	crawlImage("computer")	
	#crawlImage("notebook", r"D:\TEMP\python_download\7")
