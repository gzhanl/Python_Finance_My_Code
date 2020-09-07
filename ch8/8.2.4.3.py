from selenium import webdriver

import time

browser=webdriver.Chrome()

browser.get('https://www.baidu.com')

browser.find_element_by_xpath('//*[@id="kw"]').send_keys('python')

browser.find_element_by_xpath('//*[@id="su"]').click()

"""
留时间等网页完全打开
"""
time.sleep(3)  #  delay 3 sec


data=browser.page_source

print(data)

