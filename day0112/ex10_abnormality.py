import pandas as pd
import numpy as np

df = pd.DataFrame({'sex'   : [1, 2, 1, 3, 2, 1],
                   'score' : [5, 4, 3, 4, 2, 6]})

df['sex']=np.where(df['sex']==3, pd.NA, df['sex'])
print(df)

df['score']=np.where(df['score']>5, pd.NA, df['score'])
print(df)

# df=df.dropna(subset=['sex','score'])
# print(df)

# df.sex = df.sex.astype(int)
# df.score = df.score.astype(int)
# df=df.astype(int)
print(df)

