from selenium import webdriver

chrome_options=webdriver.ChromeOptions()

chrome_options.add_argument('--headless')

browser=webdriver.Chrome(options=chrome_options)

browser.get('https://finance.sina.com.cn/realstock/company/sh000001/nc.shtml')

data=browser.page_source

print(data)

browser.quit()