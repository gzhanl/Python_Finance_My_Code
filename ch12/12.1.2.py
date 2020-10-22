# 它可能会弹出一个Warning警告，警告不是报错，不用在意
import pandas as pd
from selenium import webdriver
import re
# 设置Selenium的无界面模式
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)

'''如果运行代码报错，可能是因为pandas版本的原因，可以将下面的内容注释了，使用该代码文件最下面被注释的内容。'''
data_all = pd.DataFrame()  # 创建一个空列表用来汇总所有表格信息
for pg in range(1, 2):  # 可以将页码调大，比如2019-04-30该天，网上一共有176页，这里可以将这个2改成176
    #url='http://yanbao.stock.hexun.com/ybsj.aspx?type=5'
    url = 'http://yanbao.stock.hexun.com/ybsj.aspx?type=' + str(pg)
    browser.get(url)  # 通过Selenium访问网站
    data = browser.page_source  # 获取网页源代码
    table = pd.read_html(data)[0]  # 通过pandas库提取表格
    print(table)