import seaborn as sns
import matplotlib.pyplot as plt

t=sns.load_dataset('titanic')

# FacitGrid
# x, y의 값의 종류별로 화면을 분할하여 어떤 함수를 적용하여 그래프를 그리고자 할 때 사용

# 화면 분할
a=sns.FacetGrid(data=t, col='who', row='survived')    #6개의 화면으로 분할

# 각 화면에 나이의 히스토그램을 그리기
a=a.map(plt.hist,"age")
plt.show()