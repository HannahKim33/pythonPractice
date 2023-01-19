import pandas as pd
import numpy as np
mpg=pd.read_csv('../Data/mpg.csv')
print(mpg)
print(mpg.info())

#1
print("********1번********")
df1=mpg.assign(displ_lh=np.where(mpg['displ']<=4,'Low','High'))
print(df1)

df2=df1.groupby('displ_lh').agg(mean_hwy=('hwy','mean'))
print(df2)

#2
print("********2번********")
df3=mpg.query('manufacturer in ["audi","toyota"]').groupby('manufacturer')\
    .agg(mean_cty=('cty','mean'))
print(df3)

#3
print("********3번********")
#각각 평균
df4=mpg.query("manufacturer in ['chevrolet','ford','honda']")\
    .groupby('manufacturer').agg(mean_hwy=('hwy','mean'))
print(df4)
#전체 평균
df5=mpg.query("manufacturer in ['chevrolet','ford','honda']")['hwy'].mean()
print(df5)

#4
print("********4번********")
df6=mpg[['category','cty']]
print(df6)

#5
print("********5번********")
df7=df6.query("category in ['suv','compact']").groupby('category')\
    .agg(mean_cty=('cty','mean'))
print(df7)

#6
print("********6번********")
df8=mpg.copy()
df8['sum_cty_hwy']=df8['cty']+df8['hwy']
print(df8)

#7
print("********7번********")
df8['avg_cty_hwy']=df8['sum_cty_hwy']/2
print(df8)

#8
print("********8번********")
df9=df8.sort_values(by='avg_cty_hwy',ascending=False)
print(df9.head(3))

#9
print("********9번********")
df10=mpg.copy().assign(sum_cty_hwy=mpg['cty']+mpg['hwy'])\
    .assign(avg_cty_hwy=(mpg['cty']+mpg['hwy'])/2)\
    .sort_values(by='avg_cty_hwy',ascending=False).head(3)
print(df10)

#10
print("********10번********")
df11=mpg.groupby('category').agg(mean_cty=('cty','mean'))
print(df11)

#11
print("********11번********")
df12=df11.sort_values(by='mean_cty',ascending=False)
print(df12)

#12
print("********12번********")
df13=mpg.groupby('manufacturer').agg(mean_hwy=('hwy','mean'))\
    .sort_values(by='mean_hwy',ascending=False).head(3)
print(df13)

#13
print("********13번********")
df14=mpg.query('category=="compact"').groupby('manufacturer')\
    .agg(count_compact=('category','count'))\
    .sort_values(by='count_compact',ascending=False)
print(df14)