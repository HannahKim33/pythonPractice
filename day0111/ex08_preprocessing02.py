import pandas as pd
import numpy as np

exam=pd.read_csv('../Data/exam.csv')
# print(exam)

# df1=exam.assign(total=exam['math']+exam['english']+exam['science'])     #exam에는 칼럼이 추가되지 않음. 새로운 변수에 대입해야 함
# print(exam)
# print(df1)
#
# df2=exam.assign(total=exam['math']+exam['english']+exam['science'],
#                 mean=(exam['math']+exam['english']+exam['science'])/3)
#
# print(df2)
#
# df3=exam.assign(test=np.where(exam['science']>=60, 'Pass', 'Fail'))
# print(df3)
#
# #메소드 체이닝
# df4=exam.assign(total=exam['math']+exam['english']+exam['science']).sort_values('total')
# print(df4)

# df5=exam.assign(total=exam['math']+exam['english']+exam['science'])\
#     .sort_values('total',ascending=False)
# print(df5)

# df5=exam.assign(total=lambda x:x['math']+x['english']+x['science'])\
#     .sort_values('total',ascending=False)
# print(df5)

# df6=exam.assign(total=exam['math']+exam['english']+exam['science'],
#                 mean=lambda a:a['total']/3)
# print(df6)
#
# df7=exam.assign(total=lambda a:a['math']+a['english']+a['science'],
#                 mean=lambda a:a['total']/3)
# print(df7)

# 파생변수를 한 번에 여러 개 만들 때, 람다식으로 만들면 바로 전에 만든 변수를 그 다음 변수를 만들 때 활용할 수 있다. 일반식으로 만들면 활용 불가.
# ↓오류
# df6=exam.assign(total=exam['math']+exam['english']+exam['science'],
#                 mean=exam['total']/3)
# print(df6)

#수학에 대한 평균 구하기      DataFrame 타입으로. mean()은 하나의 숫자 (float) 반환.
df=exam.agg(mean_math=('math','mean'))
print(df)
print(type(df))     #DataFrame

# agg 함수는 단독으로 잘 안 씀. groupby와 같이 사용.
# 반별 수학의 평균
df=exam.groupby('nclass').agg(mean_math=('math','mean'))
print(df)
print(type(df))

# pivot_table로도 같은 결과 낼 수 있음
df2=exam.pivot_table(values='math', index='nclass', aggfunc='mean')
print(df2)
print(type(df2))

df3=exam.groupby('nclass')\
    .agg(mean_math=('math','mean'),
         sum_math=('math','sum'),
         median_math=('math','median'),
         n=('math','count'))
print(df3)

df4=exam.groupby('nclass').mean()
print(df4)