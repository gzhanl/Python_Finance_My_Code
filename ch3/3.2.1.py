# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 23:41:54 2020

@author: DELL
"""

import requests
import re
#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}  # my browser

def baidu(company):
    #url = 'https://www.baidu.com/s?tn=news&rtt=1&bsst=1&cl=2&wd=' + company  # 把链接中rtt参数换成4即是按时间排序，默认为1按焦点排序，3.4.1小节也有讲到
    
    url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=' + company  # my url

    res = requests.get(url, headers=header).text
    # print(res)

    p_info = '<p class="c-author">(.*?)</p>'
    p_href = '<h3 class="c-title">.*?<a href="(.*?)"'
    p_title = '<h3 class="c-title">.*?>(.*?)</a>'
    info = re.findall(p_info, res, re.S)
    href = re.findall(p_href, res, re.S)
    title = re.findall(p_title, res, re.S)

    source = []  # 先创建两个空列表来储存等会分割后的来源和日期
    date = []
    for i in range(len(info)):
        title[i] = title[i].strip()
        title[i] = re.sub('<.*?>', '', title[i])
        info[i] = re.sub('<.*?>', '', info[i])
        source.append(info[i].split('&nbsp;&nbsp;')[0])
        date.append(info[i].split('&nbsp;&nbsp;')[1])
        source[i] = source[i].strip()
        date[i] = date[i].strip()
        print(str(i + 1) + '.' + title[i] + '(' + date[i] + '-' + source[i] + ')')
        print(href[i])


companys = ['华能信托', '阿里巴巴', '万科集团', '百度集团', '腾讯', '京东']
for c in companys:  # 这个i只是个代号，可以换成其他内容
    baidu(c)
    print(c + '百度新闻爬取成功\n')