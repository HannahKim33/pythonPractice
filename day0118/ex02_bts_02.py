import pandas as pd
import numpy as np
import konlpy
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

df_word=pd.read_csv('../Data/bts.csv', encoding='UTF-8')

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

df_word=df_word.groupby('word',as_index=False).agg(freq=('word','count')).sort_values(by='freq', ascending=False)

# 이거안됨
# print(df_word.head(20))
# index_dh=df_word[df_word['word']=='대한'].index[0]
# df_word.loc[index_dh]['freq']=df_word.loc[index_dh]['freq']/2
# print(df_word.head(20))

df_word['word']=np.where(df_word['word']=='선양','국위선양',df_word['word'])
df_word['word']=np.where(df_word['word']=='국위','국위선양',df_word['word'])
df_word['word']=np.where(df_word['word']=='면제','군면제',df_word['word'])
df_word['word']=np.where(df_word['word']=='군대','군면제',df_word['word'])
df_word['word']=np.where(df_word['word']=='병역','군면제',df_word['word'])
df_word['word']=np.where(df_word['word']=='대한','대한민국',df_word['word'])
df_word['word']=np.where(df_word['word']=='민국','대한민국',df_word['word'])
df_word['word']=np.where(df_word['word']=='나라','대한민국',df_word['word'])
df_word['word']=np.where(df_word['word']=='한국','대한민국',df_word['word'])
df_word=df_word.groupby('word',as_index=False).aggregate({'word':'first', 'freq':'sum'})\
    .sort_values(by='freq', ascending=False)

sns.barplot(data=df_word, x='freq', y='word')
plt.show()

# print(df_word)
dic_word=df_word.set_index('word').to_dict()['freq']
# print(dic_word)

import PIL
icon=PIL.Image.open('../Data/cloud.png')

img=PIL.Image.new('RGB',icon.size,(255,255,255))
img.paste(icon,icon)
img=np.array(img)

font='../Data/DoHyeon-Regular.ttf'

wc=WordCloud(
    random_state=1234,
    font_path=font,
    width=400,
    height=400,
    background_color='white',
    mask=img
)

img_wordcloud=wc.generate_from_frequencies(dic_word)
plt.figure(figsize=(10,10))
plt.axis('off')
plt.imshow(img_wordcloud)
# plt.show()