import numpy as np
import pandas as pd
import xlrd

champs= pd.read_excel('./Data/MLB World Series Champions_ 1903-2016.xlsx')
print(champs)
# print(type(champs))

# #distinct Champion 출력
# names=champs['Champion']
# print(len(names))
# names=list(set(names))
# print(names)
# print(len(names))
#
# #두 번째 방법
# names2=champs.groupby('Champion').size().index
# print(len(names2))
#
# #3
# names3=champs['Champion'].unique()
# print(len(names3))
#
# #우승팀들의 평균 승률을 출력
# print(champs['WinRatio'].mean())
# print(champs.WinRatio.mean())
#
# #팀별로 평균 승률 출력
# a=champs.pivot_table(values='WinRatio', index='Champion')
# print(a)
#
# #100번 이상 승리한 팀들
# #나
# b=champs[champs['Wins']>=100]
# print(b['Champion'].unique())
#
# #선생님 코드
# over_100=champs['Wins']>=100
# print(over_100)     #boolean array
# print(champs[over_100])     #>=100 조건을 만족하는 레코드
# print(champs[over_100].Champion.unique())     # 그 중 Chamipon 칼럼만 출력

# #New York Yankees의 평균 승률
# ny=champs[champs['Champion']=='New York Yankees']
# print(ny.WinRatio.mean())
#
# #처음 우승한 연도
# print(ny.Year.min())
#
# #마지막 우승한 연도
# print(ny.Year.max())

# #최다 우승 5팀
# a= champs.groupby('Champion').size()
# print(a)
# a=a.sort_values(ascending=False)
# print(a)
# #문제점: 5등 동점자가 넷임
# #5번째 팀의 우승 횟수와 우승 횟수가 같거나 큰 팀들을 모두 출력
# fifth=a[4]
# top_5=a[a>=fifth]
# print(top_5)

# a=np.arange(10)
# b=np.arange(5)
# print(a)
# print(b)
# print(np.setdiff1d(a,b))
# # =>
# # [0 1 2 3 4 5 6 7 8 9]
# # [0 1 2 3 4]
# # [5 6 7 8 9]

champs_years=champs.Year.values
all_years=np.arange(champs_years[0],champs_years[-1]+1)
print(np.setdiff1d(all_years,champs_years))