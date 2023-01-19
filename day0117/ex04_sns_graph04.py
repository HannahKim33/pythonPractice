import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

t=sns.load_dataset('titanic')
# print(t)
sns.set_style('whitegrid')

fig=plt.figure(figsize=(15,5))
ax1=fig.add_subplot(1,3,1)
ax2=fig.add_subplot(1,3,2)
ax3=fig.add_subplot(1,3,3)


sns.countplot(data=t.query('survived==1'), x='sex', ax=ax1)

df1=t.groupby(['sex','class'], as_index=False)['survived'].value_counts().query('survived==1')
print(df1)
sns.barplot(data=df1, x='sex', y='survived', hue='class', ax=ax2)
sns.barplot(data=df1, x='sex', y='survived', hue='class', ax=ax3, dodge=False)
plt.show()

# df1.pivot(index='sex', columns='class', values='alive_count').plot.bar(stacked=True, rot=0, ax=ax3)



