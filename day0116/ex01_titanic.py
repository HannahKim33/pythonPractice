import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_original=sns.load_dataset('titanic')
t=df_original.copy()

# print(t.isna().sum())
# 1. 성별에 따른 생존율
# df1=t.groupby('sex', as_index=False)['alive'].value_counts(normalize=True)
# # print(df1)
#
# df1=df1.query('alive=="yes"')
# # print(df1)
# sns.barplot(data=df1, x='sex', y='proportion')
# # plt.show()
#
# # 2. 등급에 따른 생존율
# df2=t.groupby('class', as_index=False)['alive'].value_counts(normalize=True)
# # print(df2)
# df2=df2.query('alive=="yes"')
# # print(df2)
# sns.barplot(data=df2, x='class', y='proportion')
# # plt.show()

# # 3. 등급, 성별에 따른 생존율
# df3=t.dropna(subset=['sex','class','alive']).groupby(['class','sex'],as_index=False)['alive']\
#     .value_counts(normalize=True)
# # print(df3)
# df3=df3.query('alive=="yes"')[['class','sex','proportion']]
# print(df3)
# sns.barplot(data=df3, x='class', y='proportion', hue='sex')
# plt.show()

#4. 혼자 탑승/가족과 탑승 생존율
# df4=t.groupby('alone', as_index=False)['alive'].value_counts(normalize=True).query('alive=="yes"')
# # print(df4)
# sns.barplot(data=df4, x='alone', y='proportion')
# plt.show()

#5 배 요금에 따른 생존 여부
# print(t['fare'].describe())

#   그룹으로 묶기
# t['fareg']=np.where(t['fare']<8,'low',np.where(t['fare']<15,'middle-low',np.where(t['fare']<31,'middle-high','high')))
# df5=t.dropna(subset=['fare','alive']).groupby('fareg', as_index=False)['alive'].value_counts(normalize=True).query('alive=="yes"')
# print(df5)
# sns.barplot(data=df5, x='fareg', y='proportion', order=['low','middle-low','middle-high','high'])
# plt.show()

df5=t.dropna(subset=['fare','alive']).groupby(['fare','alive'], as_index=False).agg(n=('age','count'))
df5=df5.query('alive=="yes"')

sns.scatterplot(data=df5, x='fare', y='n')
plt.show()

#6 연령별 생존
# print(t['age'].describe())
# t['ageg']=np.where(t['age']<20,'minor',np.where(t['age']<40,'young',np.where(t['age']<60,'middle-aged','old')))
# df6=t.dropna(subset=['age','alive']).groupby('ageg', as_index=False)['alive'].value_counts(normalize=True).query('alive=="yes"')
# # print(df6)
# sns.barplot(data=df6, x='ageg', y='proportion', order=['minor','young','middle-aged','old'])
# plt.show()