import requests
url = 'http://search.worldbank.org/api/projects/all.csv'
res = requests.get(url)  # 只要能够获得下载链接，像Excel文件、图片文件都可以进行下载
file = open('世界银行项目表.csv', 'wb')  # 这是当前目录，可以修改所需的文件保存路径，这里得选择wb二进制的文件写入方式
file.write(res.content)
file.close()  # 通过close()函数关闭open()函数打开的文件，有助于释放内存，是个编程的好习惯
print('世界银行项目表.csv下载完毕')