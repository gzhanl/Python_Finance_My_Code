"""

提取PDF表格资料
"""

import pdfplumber
import pandas as pd
pdf = pdfplumber.open('公司A理财公告.PDF')
pages = pdf.pages
page = pages[3]  # 因为表格在第四页，所以提取第四页，也即pages[3]
tables = page.extract_tables()  # 通过extract_tables方法获取该页所有表格
table = tables[0]  # 因为第四页只有一个表格，所以通过tables[0]提取
print(tables)
print(table)