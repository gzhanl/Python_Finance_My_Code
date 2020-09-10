import requests

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}  # my browser

url='http://so.eastmoney.com/news/s?keyword=阿里巴巴'

res=requests.get(url,headers=header).text

print(res)