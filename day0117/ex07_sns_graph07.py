import seaborn as sns
import matplotlib.pyplot as plt

t=sns.load_dataset('titanic')

fig=plt.figure(figsize=(15,5))
ax1=fig.add_subplot(1,3,1)
ax2=fig.add_subplot(1,3,2)
ax3=fig.add_subplot(1,3,3)

#distplot : 단변수(하나의 변수)에 사용하며, 기본값은 히스토그램과 커널 밀도 함수(확률 밀도)를 그래프로 출력한다

#요금에 대해 히스토그램과 커널 밀도 함수를 그래프로 그리기
# hist  히스토그램 표시여부
# kde   커널 밀도 함수 표시 여부
# sns.distplot(t['fare'], ax=ax1)
sns.histplot(t['fare'], kde=True, ax=ax1)
sns.distplot(t['fare'], hist=False, ax=ax2)
sns.distplot(t['fare'], kde=False, ax=ax3)
plt.show()