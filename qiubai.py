# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
page = 1
url = 'http://www.qiushibaike.com/8hr/page/%d/?s=4908781' %page
user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"
headers = { 'User-Agent' : user_agent }
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)
back=response.read()
#print back
imglist=re.findall(r'<div[^>]class="content">\n\n([^<]+)<[^>]+.+\n\n[^<]',back)
print imglist
f = open('糗事百科'+str(page)+'.txt', 'w')
for joke in imglist:
    f.write(joke)

