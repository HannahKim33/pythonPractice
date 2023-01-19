import pandas as pd

# df_csv_exam=pd.read_csv('../Data/exam.csv')
# print(df_csv_exam)

df_midterm=pd.DataFrame({
    'english':[90,80,60,70],
    'math':[50,60,100,20],
    'nclass':[1,1,2,2]
})

print(df_midterm)

#index=값 설정하지 않으면 자동으로 인덱스 생성됨. False 하면 인덱스 생성되지 않음
df_midterm.to_csv("../Data/output_newdata.csv", index=False)