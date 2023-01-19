import seaborn as sns
import matplotlib.pyplot as plt

t=sns.load_dataset('titanic')
print(t.head())
print(t.info())

# print(t['who'].value_counts())

fig=plt.figure(figsize=(20,5))
ax1=fig.add_subplot(1,3,1)
ax2=fig.add_subplot(1,3,2)
ax3=fig.add_subplot(1,3,3)

# 1. class 의 빈도수
# 2. class의 빈도수, who를 구분
# 3. class의 빈도수, who를 구분, 누적형태
# print(t['class'].value_counts())
sns.countplot(data=t, x='class', ax=ax1)
sns.countplot(data=t, x='class', hue='who', ax=ax2)
sns.countplot(data=t, x='class', hue='who', dodge=False, ax=ax3)
plt.show()