# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 22:04:13 2020

@author: DELL
"""

# =============================================================================
# 5.1 数据去重及清洗优化 by 王宇韬
# =============================================================================

import requests
import re
import pymysql
import time

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
my_header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}  # my browser

def baidu(company):
    # 1.获取网页源代码（参考2.3、3.1、3.4节）
    url = 'https://www.baidu.com/s?tn=news&rtt=4&bsst=1&cl=2&wd=' + company  # 其中设置rtt=4则为按时间排序，如果rtt=1则为按焦点排序
    res = requests.get(url, headers=headers, timeout=10).text

    # 2.编写正则提炼内容（参考3.1节）
    p_href = '<h3 class="c-title">.*?<a href="(.*?)"'
    p_title = '<h3 class="c-title">.*?>(.*?)</a>'
    p_info = '<p class="c-author">(.*?)</p>'
    href = re.findall(p_href, res, re.S)
    title = re.findall(p_title, res, re.S)
    info = re.findall(p_info, res, re.S)

    # 3.数据清洗（参考3.1节）
    source = []  # 先创建两个空列表来储存等会分割后的来源和日期
    date = []
    for i in range(len(title)):
        title[i] = title[i].strip()
        title[i] = re.sub('<.*?>', '', title[i])
        info[i] = re.sub('<.*?>', '', info[i])
        source.append(info[i].split('&nbsp;&nbsp;')[0])
        date.append(info[i].split('&nbsp;&nbsp;')[1])
        source[i] = source[i].strip()
        date[i] = date[i].strip()

        # 统一日期格式（参考5.1节）
        date[i] = date[i].split(' ')[0]
        date[i] = re.sub('年', '-', date[i])
        date[i] = re.sub('月', '-', date[i])
        date[i] = re.sub('日', '', date[i])
        if ('小时' in date[i]) or ('分钟' in date[i]):
            date[i] = time.strftime("%Y-%m-%d")
        else:
            date[i] = date[i]

    # 4.正文爬取及数据深度清洗（参考5.1和5.2和5.3节）
    for i in range(len(title)):
        # 获取新闻正文
        try:
            article = requests.get(href[i], headers=headers, timeout=10).text
        except:
            article = '单个新闻爬取失败'
        # 数据深度清洗
        company_re = company[0] + '.{0,5}' + company[-1]  # 匹配“公司名称第一个字 + 0到5个任意字符 + 公司最后一个字”这样的匹配规则
        if len(re.findall(company_re, article)) < 1:
            title[i] = ''
            source[i] = ''
            href[i] = ''
            date[i] = ''
    while '' in title:
        title.remove('')
    while '' in href:
        href.remove('')
    while '' in date:
        date.remove('')
    while '' in source:
        source.remove('')

    # 5.打印清洗后的数据（参考3.1节）
    for i in range(len(title)):
        print(str(i + 1) + '.' + title[i] + '(' + date[i] + ' ' + source[i] + ')')
        print(href[i])

    # 6.将数据存入数据库及数据去重（参考4.4节和5.1节）
    for i in range(len(title)):
        db = pymysql.connect(host='localhost', port=3306, user='root', password='', database='pachong', charset='utf8')
        cur = db.cursor()  # 获取会话指针，用来调用SQL语句

        # 6.1 查询数据，为之后的数据去重做准备
        sql_1 = 'SELECT * FROM test WHERE company =%s'
        cur.execute(sql_1, company)
        data_all = cur.fetchall()
        title_all = []
        for j in range(len(data_all)):
            title_all.append(data_all[j][1])

        # 6.2 判断数据是否在原数据库中，不在的话才进行数据存储
        if title[i] not in title_all:
            sql_2 = 'INSERT INTO test(company,title,href,source,date) VALUES (%s,%s,%s,%s,%s)'  # 编写SQL语句
            cur.execute(sql_2, (company, title[i], href[i], source[i], date[i]))  # 执行SQL语句
            db.commit()  # 当改变表结构后，更新数据表的操作
        cur.close()  # 关闭会话指针
        db.close()  # 关闭数据库链接
    print('------------------------------------')  # 分割符

# 7.批量爬取多家公司（参考3.2节）
companys = ['华能信托', '阿里巴巴', '百度集团', '腾讯', '京东']
for company in companys:
    try:
        baidu(company)
        print(company + '数据爬取并存入数据库成功')
    except:
        print(company + '数据爬取并存入数据库失败')
