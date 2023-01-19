import pandas as pd
mpg=pd.read_csv('../Data/mpg.csv')
print(mpg)

df=mpg.groupby(['manufacturer','drv'])\
    .agg(mean_cty=('cty','mean'))
print(df)

#audi의 drv 별로 빈도수 출력
df2=mpg.query("manufacturer=='audi'")\
    .groupby('drv')\
    .agg(n=('drv','count'))
print(df2)