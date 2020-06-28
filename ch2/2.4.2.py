# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:18:44 2020

@author: DELL
"""

import re
res = '文本A百度新闻文本B'
source = re.findall('文本A(.*?)文本B', res)
print(source)