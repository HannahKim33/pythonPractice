import seaborn as sns
import matplotlib.pyplot as plt

t=sns.load_dataset('titanic')

# jointplot: 산점도를 기본으로 표시하고 x-y 축에 각 변수에 대한 히스토그램을 동시에 보여주는 함수
#           두 변수 사이의 관계와 값의 분포도(값이 분산되어 있는 정도)를 동시에 확인할 수 있다.
# x: fare, y: age 에 대하여 산점도와 히스토그램을 동시에 확인해보자
# 회귀선: kind="reg"
# 육각형 산점도: kind="hex"
# 커널밀도함수 : kind="kde"
sns.jointplot(data=t, x='fare', y='age')
# sns.jointplot(data=t, x='fare', y='age', kind='reg')
sns.jointplot(data=t, x='fare', y='age', kind='hex')
plt.show()