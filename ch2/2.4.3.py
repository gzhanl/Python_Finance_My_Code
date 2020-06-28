# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:59:39 2020

@author: DELL
"""

import re
res = '<h3>文本C <fsdfdsf变化的网址sdfsdf> 文本D新闻标题</h3>'
p_title = '<h3>文本C.*?文本D(.*?)</h3>'
title = re.findall(p_title, res)
print(title)
