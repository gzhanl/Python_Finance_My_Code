from selenium import webdriver

browser=webdriver.Chrome()

browser.get('https://www.baidu.com')

browser.find_element_by_xpath('//*[@id="kw"]').send_keys('python')

browser.find_element_by_xpath('//*[@id="su"]').click()

#browser.quit()