import pandas as pd

mpg=pd.read_csv('../Data/mpg.csv')
#['CNC','diesel','ethanol E85','premium','regular']
price_fl=pd.DataFrame({'fl':['c','d','e','p','r'],
                         'price_fl':[2.35,2.38,2.11,2.76,2.22]})
print(price_fl)
print(mpg['fl'].value_counts())

df=pd.merge(mpg, price_fl, on='fl')
print(df[['model','fl','price_fl']].head())

