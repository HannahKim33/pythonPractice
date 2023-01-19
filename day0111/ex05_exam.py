import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('../Data/exam.csv')
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.describe())

df=df.rename(columns={'math':'MATH', 'english':'ENG','science':'SCI'})
print(df.head())

df['sum']=df[['MATH','ENG','SCI']].sum(axis=1)
df['avg']=df[['MATH','ENG','SCI']].mean(axis=1)
print(df)

count_class=df['nclass'].value_counts()
print(count_class)

df['PF']=np.where(df['avg']>=60,'P','F')
print(df)

df['grade']=np.where(df['avg']>=90,'A',
                     np.where(df['avg']>=80,'B',
                              np.where(df['avg']>=70,'C',
                                       np.where(df['avg']>=60,'D','F'))))
print(df)

count_grade=df['grade'].value_counts().sort_index()
count_grade.plot.bar(rot=1)
plt.show()