import pandas as pd
import numpy as np

# # 팀별연습) (선생님 풀이)
# #
# # << 실습1 >>
# # 실습을 위하여 mpg데이터의 다음의 위치에 결측치를 만들어 봅니다.
# # 64,123,130,15,211 행의 고속도로 연비
# mpg=pd.read_csv('../Data/mpg.csv')
# print(mpg.isna().sum())
# mpg.loc[[64,123,130,15,211],['hwy']]=pd.NA
# print(mpg.isna().sum())
#
# # 1) 구동방식별로 고속도로 연비 평균이 어떻게 다른지 알아보려고 합니다.
# # 분석을 하기 전에 우선 두 변수에 결측치가 있는지 확인 합니다.
# # 구동방식과 고속도로연비 변수에 결측치가 몇개 있는지 알아봅니다.
# print(mpg.isna().sum())
# print(mpg['drv'].isna().sum())
# print(mpg['hwy'].isna().sum())
# #
# # 2) 결측치가 있으면 결측치를 제거하고 어떤 구동방식의 고속도로 연비
# #     평균이 높은지 하나의 pandas 구문으로 만들어 봅니다.
# print(mpg.dropna(subset=['hwy','drv']).groupby('drv').agg(mean_hwy=('hwy','mean'))\
#     .sort_values(by='mean_hwy', ascending=False))
# ---------------------------------------------------------------
#
# << 실습2 >>
# # 실습을 위하여 mpg데이터를 다시 읽어와 다음의 위치에 이상치를 만들어 봅니다.
mpg=pd.read_csv('../Data/mpg.csv')

# 9,13,57,92 행의 구동방식을 "k"
# mpg.loc[[9,13,57,92],['drv']]='k'
# print("결측치 수: ",mpg['drv'].isna().sum())
# 구동 방식은 f,4,r 범주 내에 있어야 한다. --> 범주형 데이터
# 범주형 데이터에 대해 이상치가 있는지 확인하려면 각 종류별로 빈도수를 파악한다. value_counts()

# # 28,42,128,202 행의 도시연비를 차례대로 3,4,39,42
mpg.loc[[28,42,128,202],['cty']]=[3,4,39,42]

#
# 1) 구동방식에 이상치가 있는지 확인 해 봅니다.
#     이상치를 결측치 처리 한 다음 이상치가 사라 졌는지 확인 합니다.
# print(mpg['drv'].value_counts())
# mpg['drv']=np.where(mpg['drv']=='k',pd.NA,mpg['drv'])
# mpg['drv']=np.where(((mpg['drv']=='f') | (mpg['drv']=='4') | (mpg['drv']=='r')),mpg['drv'],pd.NA)
# mpg['drv']=np.where(mpg['drv'].isin(['f','4','r']),mpg['drv'],pd.NA)
# print(mpg['drv'].value_counts())
# print("결측치 수: ",mpg['drv'].isna().sum())
# 2) 상자그림을 이용하여 도시연비에 이상치가 있는지 확인합니다.
#         상자그림을 기준으로 정상 범위를 벗어난 값을
#         결측치 처리 합니다.
#         다시 상자그림을 그려 이상치가 사라졌느지 확인합니다.
import seaborn as sns
import matplotlib.pyplot as plt
sns.boxplot(data=mpg,y='cty')
plt.show()

#1사분위
pct25=mpg['cty'].quantile(.25)
#3사분위
pct75=mpg['cty'].quantile(.75)
#사분위
IQR=pct75-pct25
#극단치 하한 경계값
limit_down=pct25-(IQR*1.5)
#극단치 상한 경계값
limit_up=pct75+(IQR*1.5)
#극단치 몇 개인지 파악
print(len(mpg.query('cty<@limit_down')))
print(len(mpg.query('cty>@limit_up')))

mpg['cty']=np.where((mpg['cty']<limit_down)|(mpg['cty']>limit_up),np.nan,mpg['cty'])
# pd.NA로 하면 자료형이 object로 바뀌어서 boxplot을 그릴 수 없음
print("도시연비 결측치 수: ",mpg['cty'].isna().sum())

sns.boxplot(data=mpg, y='cty')
plt.show()
# ↑ 도시연비 같은 연속형 자료에 이상치가 있는지 파악하기 위해 value_counts()를 사용하는 것은 부적합하다.
# boxplot을 사용



# 3) 두변수의 이상치를 제거한 다음 구동방식별로
#         도시연비의 평균이 어떻게 다른지 하나의 pandas 구문으로
#         표현 해 봅니다.

print(mpg.dropna(subset=['drv','cty']).groupby('drv').agg(mean_cty=('cty','mean')))
