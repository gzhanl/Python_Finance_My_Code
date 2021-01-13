"""
获取多天的 前10 分钟 数据
获取股票衍生变量数据
"""

import tushare as ts
import pandas as pd

pd.set_option('display.max_rows',100)
pd.set_option('display.max_columns',50)
pd.set_option('display.width',300)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

stock_code='000002'
stock_name='万科A'
start_date='2020-10-25'
end_date='2020-10-28'
stock_k=ts.get_hist_data(stock_code,start=start_date,end=end_date)
print(stock_k)

# print(stock_k.index)
# Index(['2020-10-28', '2020-10-27'], dtype='object', name='date')

# 建立一个空的DataFrame，用于存储当前股票的信息
stock_table = pd.DataFrame()

for current_date in stock_k.index:

    # # 通过loc定位K线图中对应current_date这天的行数据
    current_k_line=stock_k.loc[current_date]

    df = ts.get_tick_data(stock_code, date=current_date, src='tt')

    df['time'] = pd.to_datetime(current_date + ' ' + df['time'])

    t = pd.to_datetime(current_date).replace(hour=9, minute=40)

    df_10=df[df['time']<t]

    #vol=df_10.volume.sum()
    vol = df_10['volume'].sum()

    # 存入字典
    current_stock_info= {
    '名称': stock_name,
    '日期': pd.to_datetime(current_date),
    '开盘价': current_k_line.open,
    '收盘价': current_k_line.close,
    '股价涨跌幅(%)': current_k_line.p_change,
    '10分钟成交量': vol
    }

    # 通过append的方式增加新的一行，忽略索引
    stock_table = stock_table.append(current_stock_info, ignore_index=True)


# 设置列的顺序
col_order = ['名称', '开盘价', '收盘价', '股价涨跌幅(%)', '10分钟成交量']
stock_table = stock_table[col_order]

print(stock_table)


'''2.下面开始获得股票衍生变量数据'''

# 通过公式1获取成交量涨跌幅
stock_table['昨日10分钟成交量'] = stock_table['10分钟成交量'].shift(-1)
stock_table['成交量涨跌幅1(%)'] = (stock_table['10分钟成交量']-stock_table['昨日10分钟成交量'])/stock_table['昨日10分钟成交量']*100
print(stock_table)


# 通过公式2获得成交量涨跌幅
ten_mean = stock_table['10分钟成交量'].sort_index().rolling(10, min_periods=1).mean()
stock_table['10分钟成交量10日均值'] = ten_mean
stock_table['成交量涨跌幅2(%)'] = (stock_table['10分钟成交量']-stock_table['10分钟成交量10日均值'])/stock_table['10分钟成交量10日均值']*100

print(stock_table)