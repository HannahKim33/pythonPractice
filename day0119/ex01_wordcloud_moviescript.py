import pandas as pd
import numpy as np
import konlpy
import re
from wordcloud import WordCloud

text=open('../Data/movie_script.txt', mode='r', encoding='UTF-8').read()

text=re.sub('[^가-힣]', ' ', text)

hannanum=konlpy.tag.Hannanum()
nouns=hannanum.nouns(text)
print(nouns)