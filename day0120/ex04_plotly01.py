import pandas as pd
import matplotlib.pyplot as plt
mpg=pd.read_csv('../Data/mpg.csv')
print(mpg)

# #동적그래프를 위한 plotly를 사용합니다
import plotly.express as px
#
# #plotly를 이용하여 산점도를 찍어봅니다
# a=px.scatter(data_frame=mpg, x='cty', y='hwy', color='drv')
# a.show()

# #막대그래프
# #자동차 종류별 빈도수
# df=mpg.groupby('category', as_index=False).agg(n=('category','count'))
# print(df)
# px.bar(data_frame=df, x='category', y='n')

#선그래프
ec=pd.read_csv('../Data/economics.csv')

#연도에 따른 개인저축률의 변화는 선그래프로 그리기
# a= px.line(data_frame=ec, x='date', y='psavert')
# a.show()

#상자그림
# a= px.box(data_frame=mpg, x='cty', y='hwy', color='drv')
# a.show()

a= px.scatter(data_frame=mpg, x='cty', y='hwy', color='drv', width=600, height=400)
a.write_html('mpg.html')