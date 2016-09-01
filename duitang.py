# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
i=0
page = 1
url = 'http://www.duitang.com/album/?id=80174265'
user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0"
headers = { 'User-Agent' : user_agent }
request = urllib2.Request(url,headers=headers)
response = urllib2.urlopen(request)
back=response.read()
imglist=re.findall(r'(http://img[^"]+\.jpeg)"',back)
for img in imglist:
    headers = {
        'Referer': 'http://www.duitang.com/album/?id=80174265',
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/" +
                      "537.36 (KHTML, like Gecko) Chrome/50.0.2661.87 Safari/537.36"}
    print img

    f=open('堆糖图片'+str(i)+'.jpg','w')
    request = urllib2.Request(img, headers=headers)
    imgposition = urllib2.urlopen(request)
    imgget = imgposition.read()
    f.write(imgget)
    i=i+1


