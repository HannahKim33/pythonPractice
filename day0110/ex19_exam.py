import pandas as pd
exam=pd.read_csv('../Data/exam.csv')
print(exam.head(1))
print(exam.tail(1))
print(exam.shape)   #몇 행 몇 열인지 반환 (20,5)
print(exam.info())
print(exam.describe())