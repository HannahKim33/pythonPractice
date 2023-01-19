import pandas as pd
import numpy as np
import konlpy
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import seaborn as sns

df=pd.read_csv('../Data/news_comment_BTS.csv', encoding='UTF-8')
# print(df)
# print(df.info())
# print(df.head(1).info())

# Data columns (total 5 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   reg_time  1 non-null      object
#  1   reply     1 non-null      object
#  2   press     1 non-null      object
#  3   title     1 non-null      object
#  4   url       1 non-null      object

# print(df['reg_time'])
# print(df['reply'])
# print(df['press'])
# print(df['title'])

# print(df['reply'])
# 한글을 제외한 모든 문제를 공백으로 처리
df['reply']=df['reply'].str.replace("[^가-힣]", " ", regex=True)

#불용어 처리
stop_word=['방탄','소년단','방탄소년단','가수','사람','생각','우리']
for w in stop_word:
    df['reply']=df['reply'].str.replace(w, " ")

#유의어 처리
# original_word=[' 면제',' 군대',' 선양',' 국위',' 나라','대한 민국',' 한국',' 대박',' 진짜']
# new_word=['군면제','군면제','국위선양','국위선양','대한민국','대한민국','대한민국','최고','최고']
#
# for i in range(len(original_word)):
#     df['reply'] = df['reply'].str.replace(original_word[i], new_word[i])

# print(df['reply'].head())

#konlpy.tag.Kkma : 문법 지키지 않은 문장들에서 단어 추출하기에 더 적합함
kkma=konlpy.tag.Kkma()
nouns=df['reply'].apply(kkma.nouns)

nouns=nouns.explode()
# print(nouns)

df_word=pd.DataFrame({'word':nouns})
df_word['wcount']=df_word['word'].str.len()
df_word=df_word.query('wcount>=2')

# csv 파일로 저장하기
df_word.to_csv('../Data/bts.csv',mode='w',header=True)
print('저장완료')

