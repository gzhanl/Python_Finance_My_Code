import  pandas as pd


url='http://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/dzjy/index.phtml'

table=pd.read_html(url)
print(table)
#table[0].to_excel('大宗交易.xlsx')