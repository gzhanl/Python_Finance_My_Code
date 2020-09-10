from selenium import webdriver

chrome_options=webdriver.ChromeOptions()

chrome_options.add_argument('--headless')

browser=webdriver.Chrome(options=chrome_options)

browser.get('http://so.eastmoney.com/news/s?keyword=阿里巴巴')

data=browser.page_source

print(data)

browser.quit()