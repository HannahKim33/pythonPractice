import pandas as pd

# df_raw=pd.DataFrame({
#     'var1':[1,2,1],
#     'var2':[2,3,2]
# })
#
#
# df_new=df_raw.copy()
#
# df_new=df_new.rename(columns={'var2':'v2','var1':'v1'})
# print(df_raw)
# print(df_new)

df=pd.DataFrame({
    "var1":[4,3,8],
    "var2":[2,6,1]
})
print(df)
df['var_sum']=df['var1']+df['var2']
print(df)

df['var_mean']=(df['var1']+df['var2'])/2
# df['var_mean']=df.min(axis=1)
print(df)