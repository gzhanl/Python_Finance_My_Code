# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 00:28:21 2020

@author: DELL
"""

# =============================================================================
# 4.3.3 数据插入数据库 by 王宇韬
# =============================================================================

# 先预定义些变量
company = '阿里巴巴'
title = '测试标题'
href = '测试链接'
source = '测试来源'
date = '测试日期'

# 连接数据库
import pymysql
db = pymysql.connect(host='localhost', port=3308, user='root', password='', database='pachong', charset='utf8')

# 插入数据
cur = db.cursor()  # 获取会话指针，用来调用SQL语句

sql = 'INSERT INTO test(company, title, href, source, date) VALUES (%s, %s, %s, %s, %s)'  # 编写SQL语句
cur.execute(sql, (company, title, href, source, date))  # 执行SQL语句

'''直接执行 sql 方式
sql = " INSERT INTO test(company, title, href, source, date) VALUES ('阿里巴巴', '测试1', '测试2', '测试3', '测试4') "  # 编写SQL语句
cur.execute(sql)  # 执行SQL语句
'''

db.commit()  # 当改变表结构后，更新数据表的操作
cur.close()  # 关闭会话指针
db.close()  # 关闭数据库链接
