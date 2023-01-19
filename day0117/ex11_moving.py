import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.xticks(rotation=45)

df=pd.read_excel('../Data/시도별 전출입 인구수.xlsx', header=0)
# print(df)
df=df.fillna(method='ffill')

print(df.head())
# print(df.shape)
# print(df.info())

#방법1

# df2=df.query('전출지별=="서울특별시" & 전입지별=="경기도"')
# df3=df2.transpose()
#
# df3=df3.iloc[2:]
# df3.columns=["n"]
# print(df3)
#
# df3.index=pd.to_datetime(df3.index)
# print(df3)
#
# sns.lineplot(data=df3, x=df3.index, y='n')
# plt.show()

#방법2
# print(df2.keys()[2:])
# years=df2.keys()[2:]
# print(df2.values[0][2:])
# counts=df2.values[0][2:]
#
# df3=pd.DataFrame({'years':years,'counts':counts})
# print(df3)
# df3['years']=pd.to_datetime(df3['years'])
#
# sns.lineplot(data=df3, x='years', y='counts')
# plt.show()

