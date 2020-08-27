import pandas as pd
import tushare as ts

# 1 保存股价数据
data = ts.get_hist_data('000002', start='2018-09-01', end='2018-12-01')
data.to_excel('share.xlsx')  # 存储到本地的share.xlsx
print('数据保存成功')


# 2 匹配估计与舆情评分
score = pd.read_excel('score.xlsx')  # 读取评分数据
share = pd.read_excel('share.xlsx')  # 读取股价数据
share = share[['date', 'close']]  # 只需要股价数据里的日期和收盘价


data = pd.merge(score, share, on='date', how='inner')  # 数据合并
data = data.rename(columns={'close': 'price'})  # close列重命名为price
data.to_excel('data.xlsx', index=False)  # 将结果导出为Excel文件
print('数据合并成功')