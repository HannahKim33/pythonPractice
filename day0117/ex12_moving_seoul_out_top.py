import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/gulim.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# plt.xticks(rotation=45)

df=pd.read_excel('../Data/시도별 전출입 인구수.xlsx', header=0)
df=df.fillna(method='ffill')

print(df.head())

df=df[df['전출지별']=='서울특별시']
df=df.loc[21:]
year_list=np.arange(2000,2011)
year_list=list(map(str,year_list))
df['total']=df[year_list].sum(axis=1)
df=df.rename(columns={'전입지별':'city'})
df=df[df['city']!='세종특별자치시']
df=df.sort_values(by='total', ascending=False).head()
df=df.set_index('city')
df=df.drop(columns=['전출지별'])
df=df.transpose()
df['인천광역시']=np.where(df['인천광역시']=='-',0,df['인천광역시'])
df['total_per_year']=df.sum(axis=1)
df=df[:-1]
print(df)

sns.lineplot(data=df, x=pd.to_datetime(df.index), y='total_per_year')
plt.show()