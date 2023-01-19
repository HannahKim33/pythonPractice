import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

t=sns.load_dataset('titanic')
# print(t)

# heatmap : 2개의 범주형 변수에 대해 각각 x, y 축에 놓고, 데이터를 매트릭스 형태로 분류해주는 그래프
# x=class, y=sex, 사람수

# 히트맵을 그리기 위한 pivot table을 만든다
df=pd.pivot_table(data=t, index='sex', columns='class', aggfunc='size')
print(df)

sns.heatmap(data=df, 
            annot=True # 값을 표시
            , fmt='d'     # 지수형태로 나타나는 값을 정수로 표시
            , linewidths=2
            , cmap='coolwarm'   #색깔 지정
            , cbar=False        #color bar 표시 X
            )
plt.show()