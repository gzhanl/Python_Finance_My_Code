"""

自动下载 PDF

"""

from selenium import webdriver
import re
import time
browser = webdriver.Chrome()

url='http://www.cninfo.com.cn/new/disclosure/detail?stockCode=300702&announcementId=1208451740&orgId=9900026797&announcementTime=2020-09-17'

browser.get(url)

browser.find_element_by_xpath('//*[@id="sub-line"]/span[1]').click()