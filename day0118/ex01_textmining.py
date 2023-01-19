moon=open('../Data/speech_moon.txt', encoding='UTF-8').read()

import re
moon=re.sub('[^가-힣]', ' ', moon)
# print(moon)
# print(type(moon))

# 불용어(분석에서 제외시키고자 하는 단어) 처리
stop_word=['나라','국민','우리','대통령','대한민국','정치','우리나라','정부']
for w in stop_word:
    moon=re.sub(w, ' ', moon)

# 복지, 복지국가 => 합치기
moon=re.sub('복지국가','복지',moon)

# 한글 형태소 분석을 위한 konlpy를 import
# konlpy는 jdk를 필요로 한다.
# jdk를 설치하고 환경변수에 JAVA_HOME에 jdk 경로를 설정 (program files-java-jdk19)
# path: %JAVA_HOME%bin
# 환경변수를 설정하고 파이참을 다시 시작해야 적용된다.
import konlpy

# hannanum: 문장속에 있는 명사만 추출
hannanum=konlpy.tag.Hannanum()

# hannanum 객체의 nouns를 활용하면 명사만 추출할 수 있다.
# 매개변수 타입: str, 반환 타입: str
# nouns=hannanum.nouns("대한민국의 영토는 한반도와 그 부속도서로 한다.")
# print(nouns)

nouns=hannanum.nouns(moon)
# print(nouns)

# 단어별 빈도수를 구하려고 함
# list를 데이터 프레임으로 변환
import pandas as pd
df_word=pd.DataFrame({'word':nouns})
# print(df_word)


# 글자 수 추가
df_word['count']=df_word['word'].str.len()
# print(df_word)
# print(df_word.shape)
df_word=df_word[df_word['count']>=2]
# print(df_word.shape)

# print(df_word.value_counts())
df_word=df_word.groupby('word', as_index=False).agg(n=('word','count')).sort_values('n', ascending=False)
# print(df_word)

import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

# 빈도수가 높은 상위 20개의 단어를 뽑아 저장
top20=df_word.head(20)

# 가로막대로 출력
# sns.barplot(data=top20, x='n', y='word')
# plt.show()

# 워드클라우드 (단어별 빈도수가 높은 순서대로 글자를 크게 출력)
#   워드클라우드에서 사용할 글꼴파일의 경로를 설정
font="../Data/DoHyeon-Regular.ttf"
#   워드클라우드를 만드는 함수는 단어별 빈도수가 있는 딕셔너리를 매개변수로 주어야 한다.
#   위에서 만든 데이터프레임을 딕셔너리로 변환     key: word   value: n(빈도수)
dic_word=df_word.set_index('word').to_dict()['n']
# print(dic_word)

from wordcloud import WordCloud
#워드클라우드 객체 만들기
# wc=WordCloud(
#     random_state=1234,
#     font_path=font,
#     width=400,
#     height=400,
#     background_color='white'
# )

# #워드클라우드 단어별 빈도수 데이터를 설정
# img_wordcloud=wc.generate_from_frequencies(dic_word)
#
# #워드클라우드 출력
# plt.figure(figsize=(10,10)) #크기 설정
# plt.axis('off') #테두리 선 없애기
# plt.imshow(img_wordcloud)
# plt.show()

import PIL
icon=PIL.Image.open('../Data/cloud.png')

import numpy as np
img=PIL.Image.new('RGB',icon.size,(255,255,255))
img.paste(icon, icon)
img=np.array(img)
# print(img)
# print(img.shape)

wc=WordCloud(
    random_state=1234,      #랜덤 노. 항상 똑같이
    font_path=font,
    width=400,
    height=400,
    background_color='white',
    mask=img,
    colormap='Wistia'
)

img_wordcloud=wc.generate_from_frequencies(dic_word)
plt.figure(figsize=(10,20))
plt.axis('off')
plt.imshow(img_wordcloud)
plt.show()