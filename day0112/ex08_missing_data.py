import pandas as pd
import numpy as np

#np.nan = 결측치를 할당
df=pd.DataFrame({
    'sex':['M','F',np.nan,'M','F'],
    'score':[5,4,3,4,np.nan]
})
print(df)
#    sex  score
# 0    M    5.0
# 1    F    4.0
# 2  NaN    3.0
# 3    M    4.0
# 4    F    NaN

#결측치를 제거하거나 다른 값으로 대체해야 함

#결측치가 있는지 확인하기  (boolean array 반환)
print(pd.isna(df))

#각 속성별 결측치 몇개인지 확인
print(pd.isna(df).sum())

