import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

mpg=pd.read_csv('../Data/mpg.csv')
print(mpg)

# 각 차마다 시티+하이웨이 연비 평균을 구해서 칼럼을 추가
mpg['total']=(mpg['cty']+mpg['hwy'])/2
# print(mpg.head())

#모든 차들의 연비의 평균
# print(sum(mpg['total'])/len(mpg))
# print(mpg['total'].mean())

# total 칼럼의 평균, 중간값, 최소값 등의 정보들을 출력
# print(mpg['total'].describe())

# mpg['total'].plot.hist()
# plt.show()

# np.where(조건, a, b) : 조건이 참이면 a. 거짓이면 b    (삼항연산자와 비슷함)
mpg['test']=np.where(mpg['total']>=20, 'pass', 'fail')
# print(mpg.head())
# print(mpg.tail())

#test 속성의 값의 종류별로 개수를 알려준다.
count_test=mpg['test'].value_counts()
# print(count_test)
# pass    128
# fail    106

# rot=0 하면 글씨를 가로로 표현
# count_test.plot.bar(rot=0)
# plt.show()

# where문 중첩
# A,B,C로 등급 매기기
mpg['grade']=np.where(mpg['total']>=30,"A",np.where(mpg['total']>=20,"B","C"))
print(mpg.head())

# 각 등급이 몇 개인지 세기
# count_grade=mpg['grade'].value_counts()
# count_grade=mpg['grade'].value_counts().sort_index()
# print(count_grade)
# print(type(count_grade))        #Series
# count_grade.plot.bar(rot=0)
# plt.show()

# df=mpg['grade']
# # print(df)
# # print(type(df))     #Series
# df=df.value_counts()
# # print(df)
# # print(type(df))     #Series
# df=df.sort_index()
# print(df)
# print(type(df))     #Series

# 메소드 체이닝 (위와 같은 결과)
# df=mpg['grade'].value_counts().sort_index()
# print(df)
# print(type(df))

mpg['grade2']=np.where(mpg['total']>=30,'A',
                       np.where(mpg['total']>=25,'B',
                                np.where(mpg['total']>=20,'C','D')))

count_grade2=mpg['grade2'].value_counts().sort_index()
print(count_grade2)
# count_grade2.plot.bar(rot=0)
# plt.show()

print(mpg['category'].value_counts())
# mpg['size']=np.where((mpg['category']=='compact') |
#                      (mpg['category']=='subcompact') |
#                      (mpg['category']=='2seater'),
#                      'small','large')
mpg['size']=np.where(mpg['category'].isin(['compact','subcompact','2seater']),
                     'small','large')
print(mpg)
print(mpg['size'].value_counts())