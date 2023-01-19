import pandas as pd
import numpy as np


midwest=pd.read_csv('../Data/midwest.csv')

# 1 전체 인구 대비 미성년 인구 백분율 변수 추가
midwest['minor_rate']=(midwest['poptotal']-midwest['popadults'])/midwest['poptotal']*100
print(midwest[['poptotal','popadults','minor_rate']])

# 2 미성년 인구 백분율이 가장 높은 상위 5개 county의 미성년 인구 백분율을 출력
print(midwest['minor_rate'].sort_values().tail())
print(midwest['minor_rate'].sort_values(ascending=False).head())

# 3 미성년 인구 비율 등급 변수 추가, 각 등급에 몇 개의 지역이 있는지 출력
midwest['minor_rate_level']=np.where(midwest['minor_rate']>=40,'large',
                                     np.where(midwest['minor_rate']>=30,'middle','small'))
print(midwest[['minor_rate','minor_rate_level']])
print(midwest['minor_rate_level'].value_counts())

# 4 전체 인구 대비 아시아인 인구 백분율 변수를 추가하고 하위 10개 지역의 state, county, 아시아인 인구 백분율 출력
# midwest['asian_rate']=midwest['popasian']/midwest['poptotal']*100
# print(midwest.sort_values(by='asian_rate')[['state','county','asian_rate']].head())

print(midwest.assign(asian_rate=midwest['popasian']/midwest['poptotal']*100)\
      .sort_values(by='asian_rate')[['state','county','asian_rate']].head())

