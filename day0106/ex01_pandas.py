import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("./Data/scores.csv")
# print(df)
# print(type(df))
# print("index:",df.index)
# print("columns:",df.columns)
# print("values:",df.values)
#
# print(df['name'])
# print(df.name)      #위와 같은 결과. 이름 열만 출력

# name=df.name
# print(name)
# print(type(name))

# a=df.iloc[0]
# print(a)
# print(type(a))

#인덱스를 학생의 이름으로 변경하기
df.index=df.name
#학생 이름이 인덱스가 되었으니 컬럼에서는 삭제한다.
del df['name']
print(df)

#첫번째 학생 'adam'의 데이터를 출력
# print(df.loc['adam'])
# print(df.iloc[0])

# #클래스가 1인 사람들의 데이터 출력
# a=df[df['class']==1]
# print(a)
#
# #클래스가 2인 사람들의 데이터 출력
# b=df[df['class']==2]
# print(b)


# print(df[['class','kor','mat']])
# subject=['kor','eng','mat']
# a=df[subject]
# print(a)

# print(df.loc['ben':'paul']) #loc은 마지막 인덱스가 포함된다
# print(df.iloc[2:7])         #iloc은 마지막 인덱스가 포함되지 않는다

# a=df.loc['ben']
# b=df.iloc[2]        #시리즈를 반환. (시리즈는 마치 자바의 map과 같음. 파이썬의 dictionary 처럼 key, value가 한 쌍으로 이루어진 자료형)
# print(a)
# print(b)
# print(a.index)      #칼럼명만
# print(a.values)     #시리즈로부터 값만 갖고 오기

# df['music']=100   #칼럼 추가하기
# print(df)

#1
class1=df[df['class']==1]
print(class1)
b=class1[['kor','mat']]
# print(b)

#2
subject=['kor','eng','mat','bio']
# b=class1[subject].sum()/len(class1)
# c=class1[subject].sum(axis=0)/len(class1)   #수직으로 평균
# d=class1[subject].sum(axis=1)/len(subject)   #수평으로 평균

#mean(): 평균을 구해주는 함수. axis=0(생략 가능): 수직 / axis=1: 수평
class1_mean=class1[subject].mean()
class1_mean_axis0=class1[subject].mean(axis=0)
class1_mean_axis1=class1[subject].mean(axis=1)
print(class1_mean)
print(class1_mean_axis0)
print(class1_mean_axis1)

#3

print('-'*50)
df['avg']=df[subject].mean(axis=1)
print(df)

#4
print('-'*50)
# sorted_df=df.sort_values('avg')               # avg 기준으로 오름차순 정렬
sorted_df=df.sort_values('avg',ascending=False) # avg 기준으로 내림차순 정렬
# sorted_df=df.sort_values(by='avg',ascending=False)    # avg 기준으로 내림차순 정렬
print(sorted_df)

print('-'*50)
print(sorted_df.head())
print(sorted_df.head(1))
print(sorted_df.tail(1))

sorted_df['avg'].plot(kind='bar')
plt.show()

