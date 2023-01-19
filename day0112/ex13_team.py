import pandas as pd
import numpy as np

# 1
mpg=pd.read_csv('../Data/mpg.csv')
mpg.loc[[64,123,130,15,211],['hwy']]=pd.NA
print(mpg.loc[[64,123,130,15,211]])

# 1-1
print(mpg[['hwy','drv']].isna().sum())

# 1-2
mpg=mpg.dropna(subset=['hwy'])
print(mpg[['hwy','drv']].isna().sum())
print(mpg.groupby('drv').agg(hwy_mean=('hwy','mean')))

# print(mpg.info())