"""
@Author:pandasgb
"""

import requests
import json
import pandas as pd
import time

'''
可用以下接口查询
http://whois.pconline.com.cn/ipJson.jsp?json=true&ip=
http://opendata.baidu.com/api.php?query='+str(ip)+'&co=&resource_id=6006&ie=utf8&oe=utf-8&format=json
http://ip.ws.126.net/ipquery?ip=
http://ip-api.com/json/14.16.139.216
'''

# #ip地址存储格式为一列
# ip = pd.read_csv('C:/Users/Administrator/Desktop/ipcode.csv',encoding='utf-8',header=None)
# ip = pd.Series(ip.iloc[:,0])
# a = []
# count = 0
# for i in ip[:]:
#     try:
#         time.sleep(0.5)
#         url = 'http://opendata.baidu.com/api.php?query='+str(i)+'&co=&resource_id=6006&ie=utf8&oe=utf-8&format=json'
#         r = requests.get(url)
#         print(count,r.status_code)
#         count += 1
#         k = json.loads(r.text)
#         ip = k['data'][0]['origip']
#         country = k['data'][0]['location']
#         all = ip+','+country
#         a.append(all)
#     except:
#         time.sleep(60)
#         continue
#
# k = pd.DataFrame(a)
# name = 'C:/Users/Administrator/Desktop/iplocation.csv'

