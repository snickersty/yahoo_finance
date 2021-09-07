#TYedit twitter
import datetime as datetime
import matplotlib.pyplot as plt
import pandas as pd
import yahoo_fin.stock_info as si
import numpy as np


tickers = ['DIA','QQQ','VTI']
start=datetime.datetime(2021,9,1)
stop=datetime.datetime(2021,9,3)
df = pd.DataFrame()
#print(df)

for i in range(len(tickers)):
 data = si.get_data(tickers[i], start_date=start, end_date=stop)['adjclose']
 df=pd.concat([df, data], axis=1)
 df.rename(columns={'adjclose': tickers[i]}, inplace=True)
#print(df)

plt.style.use('ggplot')
fig = plt.figure(figsize=(4,4))
ax = fig.add_subplot(111)
df=(df/df.iloc[0]-1)*100
df.sort_values(df.index[-1],axis=1,inplace=True)
#print(df)

# ラベルに上昇率を追加
for i in range(len(df.columns)):
 per='%.2f'%((df[df.columns[i]].iloc[-1]))
 per='↑'+per if (per[:1]!='-') else '↓'+per
 df.rename(columns={df.columns[i]: ('$')+df.columns[i]+' '+per}, inplace=True)
print(df.replace('-',''))
