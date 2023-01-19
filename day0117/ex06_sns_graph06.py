# boxplot    : 범주형 데이터의 분포와 주요 통계자료를 제공하는 함수입니다.
#              boxplot 만으로는 데이터의 퍼져있는 분산정도를 정확하게 파악하기 어렵다.
# violinplot을 이용하면 퍼져있는 분산정도를 시각적으로 파악 가능

import seaborn as sns
import matplotlib.pyplot as plt

t=sns.load_dataset('titanic')
fig=plt.figure(figsize=(20,5))
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)
ax3=fig.add_subplot(2,2,3)
ax4=fig.add_subplot(2,2,4)

df1=t.groupby(['age','sex'],as_index=False)['survived'].value_counts().sort_values(by='age')
# print(df1)

sns.boxplot(data=df1, x='survived', y='age', ax=ax1)
sns.boxplot(data=df1, x='survived', y='age', hue='sex', ax=ax2)
sns.violinplot(data=df1, x='survived', y='age', ax=ax3)
sns.violinplot(data=df1, x='survived', y='age', hue='sex', ax=ax4)
plt.show()