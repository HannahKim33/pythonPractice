import pandas as pd
import numpy as np

mpg=pd.read_csv("../Data/mpg.csv")
a= mpg['drv'].value_counts()
print(a)
print(type(a))      #Series

# mpg['drv'].value_counts().query('n>100')        #오류. Series는 query 쓸 수 없음

#to_frame: series를 DataFrame으로 변경
a=mpg['drv'].value_counts()\
    .to_frame('n')\
    .rename_axis('drv')\
    .query('n>100')
print(a)
print(type(a))