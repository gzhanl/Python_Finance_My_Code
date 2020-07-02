# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 07:51:58 2020

@author: DELL
"""

# =============================================================================
# 4.3.5 连接数据库并删除数据 by 王宇韬
# =============================================================================

import pymysql
db = pymysql.connect(host='localhost', port=3308, user='root', password='', database='pachong', charset='utf8')

company = '阿里巴巴'

cur = db.cursor()  # 获取会话指针，用来调用SQL语句

#sql = 'DELETE FROM test WHERE company = %s'  # 编写SQL语句
#cur.execute(sql, company)  # 执行SQL语句

#直接执行sql
sql = "DELETE FROM test WHERE company = '阿里巴巴' and  title = '测试1' "  # 编写SQL语句
cur.execute(sql)  # 执行SQL语句


db.commit()  # 因为改变了表结构，这一行必须要加
cur.close()  # 关闭会话指针
db.close()  # 关闭数据库链接
