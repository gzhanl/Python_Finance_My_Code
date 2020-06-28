# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 12:09:35 2020

@author: DELL
"""

import re

res='''<h3 class="c-title">
 <a href="https://baijiahao.baidu.com/s?id=1670709637927208549&amp;wfr=spider&amp;for=pc" data-click="{
      'f0':'77A717EA',
      'f1':'9F63F1E4',
      'f2':'4CA6DE6E',
      'f3':'54E5243F',
      't':'1593316477'
      }" target="_blank">
      浙江东阳<em>阿里巴巴</em>影业有限公司参与成立新公司
    </a>
</h3>
'''

p_href='<h3 class="c-title">.*?<a href="(.*?)"'

p_TITLE='<h3 class="c-title">.*?target="_blank">.*?(.*?)</a>'

href=re.findall(p_href,res,re.S)

title=re.findall(p_TITLE,res,re.S)

print(href)

print(title)