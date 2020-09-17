# =============================================================================
# 10.1 批量下载巨潮资讯网理财公告 by 王宇韬
# =============================================================================

from selenium import webdriver
import re
import time
browser = webdriver.Chrome()
url = 'http://www.cninfo.com.cn/new/fulltextSearch?notautosubmit=&keyWord=理财'
browser.get(url)
time.sleep(3)
data = browser.page_source
p_count = '<span class="total-box" style="">约(.*?)条'
count = re.findall(p_count, data)[0]  # 获取公告个数，注意这里要加一个[0],因为findall返回的是一个列表
pages = int(int(count)/10)

# 1.自动翻页获取源码源代码
datas = []
datas.append(data)  # 这边是把第一页源代码先放到datas这个列表里
for i in range(3):  # 这边为了演示改成了range(3)，想爬全部的话改成range(pages)
    browser.find_element_by_xpath('//*[@id="fulltext-search"]/div/div[1]/div[2]/div[4]/div[2]/div/button[2]').click()
    time.sleep(2)
    data = browser.page_source
    datas.append(data)
    time.sleep(1)
alldata = "".join(datas)
browser.quit()

# 2.编写正则表达式
p_title = '<span title="" class="r-title">(.*?)</span>'
p_href = '<a target="_blank" href="(.*?)" data-id='
p_date = '<span class="time">(.*?)</span>'
title = re.findall(p_title, alldata)
href = re.findall(p_href, alldata)
date = re.findall(p_date, alldata, re.S)

# 3.清洗数据
for i in range(len(title)):
    title[i] = re.sub('<.*?>', '', title[i])
    href[i] = 'http://www.cninfo.com.cn' + href[i]
    href[i] = re.sub('amp;', '', href[i])
    date[i] = date[i].strip()
    date[i] = date[i].split(' ')[0]
    print(str(i + 1) + '.' + title[i] + ' - ' + date[i])
    print(href[i])

# 4.自动筛选
for i in range(len(title)):
    if '2019' in date[i] or '2020' in date[i]:  # 筛选2019和2020年的，可以自己调节
        title[i] = title[i]
        href[i] = href[i]
        date[i] = date[i]
    else:
        title[i] = ''
        href[i] = ''
        date[i] = ''
while '' in title:
    title.remove('')
while '' in href:
    href.remove('')
while '' in date:
    date.remove('')

# 5.自动批量爬取PDF - 选择默认储存位置
for i in range(len(href)):
    browser = webdriver.Chrome()
    browser.get(href[i])
    try:
        browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[1]/a[3]').click()
        time.sleep(3)  # 这个一定要加，因为下载需要一点时间
        browser.quit()
        print(str(i+1) + '.' + title[i] + '下载完毕')
    except:
        print(title[i] + '不是PDF文件')

# 补充知识点1：无界面浏览器设置
# for i in range(len(href)):
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument('--headless')
#     browser = webdriver.Chrome(options=chrome_options)
#     browser.get(href[i])
#     try:
#         browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[1]/a[3]').click()
#         time.sleep(3)  # 这个一定要加，因为下载需要一点时间
#         browser.quit()
#         print(str(i+1) + '.' + title[i] + '是PDF文件')
#     except:
#         print(title[i] + '不是PDF文件')


# 补充知识点2：自动批量爬取PDF - 自己设定储存位置
# for i in range(len(href)):
#     chrome_options = webdriver.ChromeOptions()
#     prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\公告'} #这边你可以修改文件储存的位置
#     chrome_options.add_experimental_option('prefs', prefs)
#     browser = webdriver.Chrome(chrome_options=chrome_options)
#     browser.get(href[i])
#     try:
#         browser.find_element_by_xpath('/html/body/div/div[1]/div[2]/div[1]/a[3]').click()
#         time.sleep(3) # 这个一定要加，因为下载需要一点时间
#         print(str(i+1) + '.' + title[i] + '下载完毕')
#         browser.quit()
#     except:
#         print(title[i] + '不是PDF')
