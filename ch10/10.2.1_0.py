# 1.解析第一页的文本信息
import pdfplumber
pdf = pdfplumber.open('公司A理财公告.PDF')  # 打开PDF文件
pages = pdf.pages  # 通过pages属性获取所有页的信息，此时pages是一个列表  --->[<Page:1>, <Page:2>, <Page:3>, <Page:4>, <Page:5>]
page = pages[0]  # 获取第一页内容  page = <Page:1>
text = page.extract_text()  # 通过
print(text)  # 打印第一页内容
pdf.close()  # 关闭PDF文件