import tushare as ts
import pandas as pd

pd.set_option('display.max_rows',100)
pd.set_option('display.max_columns',50)
pd.set_option('display.width',1000)

stock_code='000002'
current_date='2020-10-27'
df=ts.get_tick_data(stock_code,date=current_date,src='tt')
print(df)

df['time']=pd.to_datetime(current_date + ' ' + df['time'])

t=pd.to_datetime(current_date).replace(hour=9,minute=40)

df_10=df[df['time']<t]

print(df_10.tail())


# 总
vol=df_10['volume'].sum()
print(vol)

