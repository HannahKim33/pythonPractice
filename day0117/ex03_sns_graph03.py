import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

t=sns.load_dataset('titanic')
# print(t)

#stripplot: 범주형 변수에 들어 있는 각 범주별 데이터의 분포를 확인할 수 있는 그래프

# 그래프 스타일 설정
sns.set_style('whitegrid')

# 나이와 클래스별로 데이터의 분포를 확인
# sns.stripplot(
#     data=t
#     , x='class'
#     , y='age'
# )
# plt.show()

# 동일한 값이 많을 경우 점이 찍힌 데에 또 찍힘
# 여기에 값이 더 많이 분포되었는지 파악하기가 어렵다.
# ====> swarmplot을 사용

# sns.swarmplot(data=t, x='class', y='age')
# plt.show()

fig=plt.figure(figsize=(10,15))
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)

sns.stripplot(data=t, x='class', y='age', ax=ax1)
sns.swarmplot(data=t, x='class', y='age', ax=ax2)
plt.show()