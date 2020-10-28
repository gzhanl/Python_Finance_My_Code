
# =============================================================================
# 12.3.2 通过Tushare库计算股票收益率
# =============================================================================

import tushare as ts
import pandas as pd
pd.set_option('display.max_rows',100)
pd.set_option('display.max_columns',50)
pd.set_option('display.width',1000)

ts_result=ts.get_hist_data('000002','2019-01-02','2019-01-31')
#print(ts_result)

start_price=ts_result.iloc[-1]['open']  # open 列的倒數 第1
end_price=ts_result.iloc[0]['close']  # close 列的第一個值
return_rate=(end_price/start_price)-1.0
print('開始日價格：',start_price)
print('結束日價格：',end_price)
print('收益率：',return_rate)