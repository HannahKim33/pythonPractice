import pandas as pd
import numpy as np

mpg=pd.read_csv("../Data/mpg.csv")

df1=mpg.query('displ<=4')['hwy'].mean()
df2=mpg.query('displ>=5')['hwy'].mean()
print(df1,df2)

print(mpg['manufacturer'].unique())