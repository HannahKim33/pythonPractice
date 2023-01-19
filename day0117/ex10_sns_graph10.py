import seaborn as sns
import matplotlib.pyplot as plt

t=sns.load_dataset('titanic')

#pairplot : 매개변수로 전달되는 변수의 리스트를 각각 행, 열로 한 만큼의 화면을 만들고
#           두 변수가 격자로 만나는 지점에 두 변수간의 관계를 산점도로 그려준다.
#           동일한 변수일 때는 히스토그램을 그려준다.

my_col=['age','pclass','fare']
a=sns.pairplot(t[my_col])
plt.show()