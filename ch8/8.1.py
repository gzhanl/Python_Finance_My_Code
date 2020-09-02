import requests
proxy = requests.get('http://api.xdaili.cn/xdaili-api//greatRecharge/getGreatIp?spiderId=b030195e2075469299bca6b661c913ff&orderno=YZ201810262456rdpAb0&returnType=1&count=1').text
proxy = proxy.strip()  # 这一步非常重要，因为要把看不见的换行符等给清除掉
print(proxy)
proxies = {"http": "http://"+proxy, "https": "https://"+proxy}
url = 'https://httpbin.org/get'
res = requests.get(url, proxies=proxies).text
print(res)