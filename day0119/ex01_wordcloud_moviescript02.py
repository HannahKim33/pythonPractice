import pandas as pd
import numpy as np
import konlpy
import re
from wordcloud import WordCloud

f=open('../Data/movie_script.txt', mode='r', encoding='UTF-8')

rows=f.readlines()
hannanum=konlpy.tag.Hannanum()
for row in rows:
    data=data+row
    i=i+1
    if i%100==0:
        data=re.sub('[^가-힣]',' ', data)
        nouns=hannanum.nouns(data)

# text=re.sub('[^가-힣]', ' ', text)
#
# hannanum=konlpy.tag.Hannanum()
# nouns=hannanum.nouns(text)
# print(nouns)


#plt.savefig('../Data/movie.png')  <- show() 대신에 파일로 저장