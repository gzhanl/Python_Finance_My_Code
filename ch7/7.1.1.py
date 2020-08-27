import  tushare as ts
import pandas as pd

pd.set_option('display.max_columns',None)

df=ts.get_hist_data('000002',start='2018-01-01',end='2019-01-31')
print(df.head(5))