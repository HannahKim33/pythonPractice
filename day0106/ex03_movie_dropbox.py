import numpy as np
import pandas as pd


pd.set_option('display.max_columns',100)

#3개의 데이터파일을 읽어 들여 하나의 데이터프레임으로 반환하는 함수를 만들고 호출해 봅니다.  완성하면 "1"
def getMovies():
    users = pd.read_csv("./Data/users.dat",
                        sep="::",
                        engine='python',
                        header=None, names=['UserID','Gender','Age','Occupation','Zip-code'])

    movies = pd.read_csv("./Data/movies.dat",
                         sep="::",
                         engine='python',
                         header=None,
                         names=['MovieID','Title','Genres'])
    ratings = pd.read_csv('./Data/ratings.dat',
                           sep="::",
                           engine='python',
                           header=None,
                           names=['UserID','MovieID','Rating','Timestamp'])
    return pd.merge(pd.merge(ratings,users),movies)

df = getMovies()
print(df.head(1))

print(df[['Gender','Age','Rating']])    #성별별로 나이별로 별점의 평균

#연습) 성별별로 나이별로 직업별로 별점의 평균을 출력 해 봅니다.    완성하면 "3"


# t5 = df.pivot_table(values='Rating', columns=['Gender','Age'])
# print(t5)

# t4 = df.pivot_table(values='Rating', index=['Gender','Age'])
# print(t4)


# t3 = df.pivot_table(values='Rating', index='Gender', columns='Age', aggfunc='mean')
# print(t3)
# print("-"*50)
# t3.columns = ["Under 18", "18-24","25-34","35-44","45-49","50-55","56+"]
# print(t3)

# t2 = df.pivot_table(values='Rating', index='Age', columns='Gender', aggfunc='mean')
# print(t2)
#
# t2.index = ["Under 18", "18-24","25-34","35-44","45-49","50-55","56+"]
# print(t2)




#연습) 남자들의 별점평균과 여자들의 별점평균을 출력 해 봅니다.        완성하면 "3"
#연습) 성별별로 별점의 평균을 출력합니다.
# t1 = df.pivot_table(values="Rating", index="Gender")
# t2 = df.pivot_table(values='Rating', columns='Gender')
# print(t1)
# print(type(t1))
# print(t2)
# print(type(t2))

# df_m = df[df['Gender'] == 'M']
# df_w = df[df['Gender'] == 'F']
# print('남자.......................')
# print(df_m)
# print('여자.......................')
# print(df_w)
# print('남자의 평균',df_m['Rating'].mean())
# print('여자의 평균',df_w['Rating'].mean())