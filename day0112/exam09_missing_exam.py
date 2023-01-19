import pandas as pd
import numpy as np

exam=pd.read_csv('../Data/exam.csv')
print(exam)
exam.loc[[2,7,14],['math']]=np.nan
print(exam)