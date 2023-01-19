import pandas as pd
import numpy as np

df=pd.DataFrame({
    'x1':[1,1,2,2]
})

# x1의 값에 따라서 1이면 'a', 그렇지 않으면 NaN을 갖는 속성 x2를 추가한다

df['x2']=np.where(df['x1']==1, 'a', pd.NA)
print(df)
print(df.isna().sum())