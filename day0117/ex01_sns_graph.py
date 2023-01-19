import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df=sns.load_dataset('titanic')
# print(df.head())
# print(df.info())

# 나이와 요금의 관계를 산점도로 나타내기
# sns.scatterplot(data=df, x='age', y='fare')
# plt.show()

# #fit_reg=False : 회귀선 그리지 않기
# sns.regplot(data=df, x='age', y='fare', fit_reg=False)
# plt.show()

# seaborn 스타일 적용
sns.set_theme(style='ticks')

# 화면을 1행 2열로 분할하여 2개의 그래프 그리기
fig=plt.figure(figsize=(15,5))      # 화면의 가로크기, 세로크기 설정

#fig 를 1행 2열로 분리했을 때의 첫번째 화면을 ax1, 두 번째 화면을 ax2로 사용
ax1=fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)

# 첫 번째 화면인 ax1에 그래프를 그리기
sns.regplot(data=df, x='age', y='fare', ax=ax1)
sns.regplot(data=df, x='age', y='fare', fit_reg=False, ax=ax2)
plt.show()

#Parameters: style: None, dict, or one of {darkgrid, whitegrid, dark, white, ticks}