import numpy as np
import pandas as pd

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
a=df[df['class']==1]
b=a[['kor','mat']]
print(b)

#2
kor=a['kor']
print(sum(kor.values)/len(kor))

#3
subs=df[['kor','eng','mat','bio']]
# print(subs.iloc[0].values)
# df['avg']=range(12)
# print(sum(subs.iloc[0].values)/len(subs.iloc[0].values)+1)

avg=[]

for i in range(len(df)):
    avg.append(sum(subs.iloc[i].values)/len(subs.iloc[i].values+1))

print(avg)
df['avg']=avg
print(df)

#4


# avg_values=df['avg'].values
# print(avg_values)


# avg_argsort=avg_values.argsort()
# print(avg_argsort)

# df.index=df.avg
# print(df)
# print(type(df))


print(df['avg'].sort_values(ascending=False))

print(df.sort_values(by='avg',ascending=False))