# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 00:40:53 2020

@author: DELL
"""

import requests


'''               Sample code
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
'''


header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}  # my browser

url='https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=阿里巴巴'

res=requests.get(url,headers=header).text

print(res)