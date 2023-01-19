import pandas as pd
exam=pd.read_csv("../Data/exam.csv")
# print(exam)
# class1=exam.query('nclass==1')
# print(class1)
#
# df=exam.query('math>=60 & science>=60 & english>=60')
# print(df)
#
# class1=exam.query('nclass==1')
# class2=exam.query('nclass==2')
#
# df=exam.query('nclass==1 | nclass==2').pivot_table(values='math', aggfunc='mean', index='nclass')
# print(df)
#
# df=pd.DataFrame({
#     'sex':['F','M','F','M'],
#     'country':['Korea','China','Japan','USA']
# })
# print(df)

# a=exam[['id','math']].query('math>=50')
# print(a)

# a=exam.query("math>=50")[['id','math']].head()
# print(a)

# a=exam.query("math>=50")\
#     [['id','math']]\
#     .head()
# print(a)

# df=exam.sort_values(['math'])
# print(df)
# print(exam)