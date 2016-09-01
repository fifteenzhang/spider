# -*- coding: utf-8 -*-
import datetime
import json
import urllib
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def getinfo(startdate, enddate,startplace,endplace):
    url = 'https://sjipiao.alitrip.com/search/cheapFlight.htm?startDate=%s&endDate=%s&' \
         'routes=%s-%s&_ksTS=1472727272319_680&callback=jsonp681&ruleId=4&flag=1' % (startdate, enddate,startplace,endplace)
    flight_html = urllib.urlopen(url).read()
    pattern = r'\(\s+(.+)\)'
    re_rule = re.compile(pattern)
    json_data = re.findall(pattern, flight_html)[0]
    flight_json = json.loads(json_data)
    flights = flight_json['data']['flights']
    return flights

def trip(flight):
        for f in flight:
            depname = '%s - ' % f['depName']
            arrname = '%s\t' % f['arrName']
            price = '\t价格：%s%s(折扣:%s)\t' % ((f['price']), f['priceDesc'], f['discount'])
            departdate = '\t日期：%s' % f['depDate']
            print depname + arrname + price + departdate

today = datetime.date.today()
delay = int(raw_input('输入数字(最多查询到45天后） 要查询几天内的机票 \n '))
enddate = today + datetime.timedelta(delay)
print enddate
endstr = str(enddate)
print '航班日期'+str(today) + ' To ' + endstr +'\n'
print '城市简称查询办法进入阿里旅行输入地点后查看网址中depCity= arrCity= \n'
startplac=raw_input('请输入出发地城市大写英文简称 eg：SHA \n')
endplac=raw_input('请输入目的地城市大写英文简称 eg：SHA \n ')
flights = getinfo(today, enddate=endstr,startplace=startplac,endplace=endplac)
print '==================以下为航班信息=================='
trip(flights)
print '================机票信息已显示完毕================\n'