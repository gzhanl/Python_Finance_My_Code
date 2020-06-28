# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:11:00 2020

@author: DELL
"""

import re
content = 'Hello 123 world 1111'


''' \d\d\d 代表找3个数字 '''
result = re.findall('\d\d\d',content)  


''' <class 'list'> '''
print(result)   

