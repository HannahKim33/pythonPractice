import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

mpg=pd.read_csv('../Data/mpg.csv')

# 값의 분포를 확인하기 위하여 "상자그림" 그리기
# 상자그림 -> 극단치 확인할 수 있음
# sns.boxplot(data=mpg, y='hwy')
# plt.show()

# 1사분위: 값을 순서대로 놓았을 때 하위 25% 값
# 2사분위: 값을 순서대로 놓았을 때 하위 50% 값
# 3사분위: 값을 순서대로 놓았을 때 하위 75% 값
# 아래수염 : 0~25%
# 위수염 : 75~100%

# 1사분위 값을 알아 봅시다
pct25=mpg['hwy'].quantile(.25)
print(pct25)    #18.0

# 3사분위 값 알아보기
pct75=mpg['hwy'].quantile(.75)
print(pct75)

# 사분범위(IQR)
iqr=pct75-pct25
print(iqr)      # 9.0

#극단치 경계값
#하한경계값 : 1사분위-사분범위 1.5
#상한경계값 : 3사분위+사분범위 1.5

lmt_dwn=pct25-iqr*1.5
lmt_up=pct75+iqr*1.5
print("하한 경계값", lmt_dwn)    #4.5
print('상한 경계값', lmt_up)     #40.5

# mpg['hwy']=np.where((mpg['hwy']>lmt_up) | (mpg['hwy']<lmt_dwn),pd.NA,mpg['hwy'])
print(mpg['hwy'].isna().sum())