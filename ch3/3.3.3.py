# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 07:16:04 2020

@author: DELL
"""

# =============================================================================
# 3.3 异常处理及24小时数据挖掘实战 by 王宇韬
# =============================================================================
import requests
import re
import time

#headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}  # my browser


def baidu(company):
    url = 'https://www.baidu.com/s?rtt=1&bsst=1&cl=2&tn=news&word=' + company
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


while True:
    companys = ['华能信托', '阿里巴巴', '万科集团', '百度集团', '腾讯', '京东']
    for c in companys:
        try:
            baidu(c)
            print(c + '百度新闻爬取成功')
        except:
            print(c + '百度新闻爬取失败')
    time.sleep(10800)  # 每10800秒运行一次，即3小时运行一次，注意缩进
