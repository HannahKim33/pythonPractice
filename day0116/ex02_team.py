import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')

kw = pd.read_spss("../Data/Koweps_hpwc14_2019_beta2.sav")
# print(kw)

df=kw.copy()
# print(df[['p1407_3aq1','p1402_8aq1']])

# df=df.rename(columns={'p1407_3aq1':'edu_code','p1402_8aq1':'월소득'})
# # print(df[['최종학력','월소득']])
# df2=df.dropna(subset=['edu_code','월소득'])[['edu_code','월소득']]
# df2=df2.sort_values(by='edu_code')
# print(df2)
#
# edu_list=pd.DataFrame({'edu_code':[1,2,3,4,5],
#                        '최종학력':['중학교 졸업 이하', '고등학교 중퇴 졸업',
#                                '전문대학 재학, 중퇴, 졸업', '대학교(4년제) 재학, 중퇴, 졸업', '대학원 이상']})
#
# df2=df2.merge(edu_list)
# print(df2)
#
# sns.scatterplot(data=df2, x='최종학력', y='월소득')
# plt.show()



# 여성 결혼율 가장 낮은 직업 10개

df = df.rename(columns = {'h14_g3':'sex', 'h14_g10':'marriage_type', 'h14_eco9':'job_code'})
df['sex']=np.where(df['sex']==1,'male','female')
df=df[['sex','marriage_type','job_code']]
# print(df)
df['marriage']=np.where(df['marriage_type']==1,'married','not_married')
# print(df)

job_list=pd.read_excel('../Data/job_list.xlsx')
# print(job_list)

df=df.merge(job_list)
# print(df)

df2=df.query('sex=="female"').dropna(subset=['job_name','marriage']).\
    groupby('job_name', as_index=False)['marriage'].value_counts(normalize=True).\
    query('marriage=="married"').sort_values(by='proportion').head(10)
print(df2)

# sns.barplot(data=df2, x='job_name', y='proportion')
# plt.show()