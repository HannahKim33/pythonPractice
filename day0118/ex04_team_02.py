import pandas as pd

f=open('../Data/seek.txt', mode='r', encoding='UTF-8')
str=''
while True:
    line = f.readline()
    if not line: break
    str+=line
f.close()

# stop_word=['.', ' and ',' to ',' a ',' for ',' the ',' or ','/','in','of']
# for w in stop_word:
#     str=str.replace(w, 'NaN')
str=str.upper()
w_list=str.split()
# print(w_list)

df=pd.DataFrame({'word':w_list})
# print(df)
df=df.groupby('word', as_index=False).agg(n=('word','count')).sort_values(by='n', ascending=False)

stop_word=['and','a','to','for','the','in','of','with','an','our','join','us','Developer','on','-','|','opportunity'\
    ,'is','looking','development','are','working','work','you','&','role','/','based','as','your','developer','will'\
           ,'exciting','be','that','company','business','their','from','contract','seeking','.NET','.Net','Work','have'\
           ,'within','part','develop','+','great','across','Developers','at','project','who','IT','or','by','month'\
           ,'this','term','make','Great','some','about','using','per','software','full','web','team','new','we',\
           'australian','currently','available']
stop_word=list(map(lambda x: x.upper(), stop_word))
df = df.drop(df[df['word'].isin(stop_word)].index)

print(df.head(50))

dic_word=df.set_index('word').to_dict()['n']
# print(dic_word)

import PIL
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

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
plt.show()