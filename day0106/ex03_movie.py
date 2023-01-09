import numpy as np
import pandas as pd

pd.set_option('display.max_columns',100)

def getMovies():
    users=pd.read_csv("./Data/users.dat", sep="::", header=None, names=['UserID','Gender','Age','Occupation','Zip-code'])
    movies=pd.read_csv("./Data/movies.dat", sep="::", header=None, names=['MovieID','Title','Genres'])
    ratings=pd.read_csv("./Data/ratings.dat", sep="::", header=None, names=['UserID','MovieID','Rating','Timestamp'])

    return pd.merge(pd.merge(ratings, users), movies)

df = getMovies()
# print(df.head(1))

#stack(): column을 index로 바꾸기
#unstack(): index를 column로 바꾸기

# t10_1=df.pivot_table(values="Rating", index="Age", columns="Gender", aggfunc="mean")
# t10_2=df.pivot_table(values="Rating", index="Age", columns="Gender", aggfunc="sum")
# print(t10_1)
# print(t10_2)
# b=pd.concat([t10_1,t10_2])
# print(b)
# c=pd.concat([t10_1,t10_2], axis=1)
# print(c)

#가장 평점평균이 높은 영화 5개 출력하기
#aggfunc 생략하면 디폴트 값이 mean
# t=df.pivot_table(values="Rating", index="Title", aggfunc="mean").sort_values(by='Rating',ascending=False)
# print(t.head(5))

# r=df[df['Title']=='Ulysses (Ulisse) (1954)']
# print(r)
#->1명이 평가해서 5점을 줌. 신뢰할 수 없는 데이터.
#평가 횟수가 500번 이상인 영화를 대상으로 하려면?

#각 영화별로 레코드의 수(각 영화별 평가수를 출력)
#select Title,count(*) from group by Title
# df2=df.groupby('Title').size()
# print(df2>=500)
# print(type(df2))    #=>series. key:Title    value:T/F
# print(df2[df2>=500].index)

#평가가 500이상인 영화 중 탑5
def getOver500(df):
    df2=df.groupby('Title').size()
    return df2[df2>=500].index

over500_index=getOver500(df)
#
# a=df.pivot_table(values='Rating', index='Title')
# a=a.loc[over500_index]
# b=a.sort_values(by='Rating',ascending=False).head(5)
# print(b)

#성별별로 영화별로 평점의 평균을 출력
by_gender=df.pivot_table(values="Rating", columns="Gender", index='Title')
print(by_gender)
print(len(by_gender))

rating_500=by_gender.loc[over500_index]
print(len(rating_500))
print(rating_500)
rating_500['diff']=rating_500['F']-rating_500['M']
print(rating_500)

#여자 평점과 남자 평점의 차이가 많은 영화 (여자가 더 좋아하는 영화 5개/남자가 더 좋아하는 영화 5개)
f_fav=rating_500.sort_values(by='diff',ascending=False)
print(f_fav.head())
print(f_fav.tail())

#호불호가 갈리지 않는 영화 5개
rating_500['Dist']=(rating_500['F']-rating_500['M']).abs()      #abs():절대값
print(rating_500)

both_fav=rating_500.sort_values(by="Dist")
print(both_fav)