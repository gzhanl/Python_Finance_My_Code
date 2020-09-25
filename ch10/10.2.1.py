# =============================================================================
# 10.2 PDF文本解析基础 by 王宇韬
# =============================================================================

# 如果直接pip install pdfplumber安装法安装失败的话，可以使用清华大学镜像安装法：pip install pdfplumber -i https://pypi.tuna.tsinghua.edu.cn/simple

# 1.解析第一页的文本信息
import pdfplumber
pdf = pdfplumber.open('公司A理财公告.PDF')  # 打开PDF文件
pages = pdf.pages  # 通过pages属性获取所有页的信息，此时pages是一个列表
page = pages[0]  # 获取第一页内容
text = page.extract_text()  # 通过
print(text)  # 打印第一页内容
pdf.close()  # 关闭PDF文件

# 2.解析全部页数的文本信息
import pdfplumber
pdf = pdfplumber.open('公司A理财公告.PDF')
pages = pdf.pages
text_all = []
for page in pages:  # 遍历pages中每一页的信息
    text = page.extract_text()  # 提取当页的文本内容
    text_all.append(text)  # 通过列表.append()方法汇总每一页内容
text_all = ''.join(text_all)  # 把列表转换成字符串
print(text_all)  # 打印全部文本内容
pdf.close()

# 3.解析表格内容
import pdfplumber
import pandas as pd
pdf = pdfplumber.open('公司A理财公告.PDF')
pages = pdf.pages
page = pages[3]  # 因为表格在第四页，所以提取第四页，也即pages[3]
tables = page.extract_tables()  # 通过extract_tables方法获取该页所有表格
table = tables[0]  # 因为第四页只有一个表格，所以通过tables[0]提取
# 替换原来table中的换行符
for i in range(len(table)):  # 遍历大列表中的每一个子列表
    for j in range(len(table[i])):  # 遍历子列表中的每一个元素
        table[i][j] = table[i][j].replace('\n', '')  # 替换换行符
pd.set_option('display.max_columns', None)  # 显示全部列
df = pd.DataFrame(table[1:], columns=table[0])  # 得到的table是嵌套列表类型，转化成DataFrame更加方便查看和分析
print(df)
pdf.close()

