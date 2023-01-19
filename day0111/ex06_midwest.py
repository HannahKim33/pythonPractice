import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df=pd.read_csv('../Data/midwest.csv')

#데이터의 특징 파악
print(df.head(1))
print(df.shape)
print(df.info())
print(df.describe())

# 칼럼 이름 수정
df=df.rename(columns={'poptotal':'total','popasian':'asian'})

# 전체 인구 대비 아시아 인구 백분율 파생변수 추가 & 히스토그램을 만들어 분포를 살펴보기
df['asian_rate']=(df['asian']/df['total'])*100
print(df[['asian','total','asian_rate']])
df['asian_rate'].plot.hist()
plt.show()

# 아시아 인구 백분율 전체 평균을 구하고 평균을 초과하면 'large', 그렇지 않으면 'small'을 부여한 파생변수 만들기
#       전체 평균
asian_rate_mean=df['asian_rate'].mean()
print(asian_rate_mean)

df['asian_rate_size']=np.where(df['asian_rate']>asian_rate_mean,'large','small')
print(df[['asian_rate','asian_rate_size']])

count_asian_rate_size=df['asian_rate_size'].value_counts()
print(count_asian_rate_size)

count_asian_rate_size.plot.bar(rot=1)
plt.show()