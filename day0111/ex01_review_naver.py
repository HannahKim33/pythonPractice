import re
import urllib.request
import json
import requests
from bs4 import BeautifulSoup

url='https://smartstore.naver.com/i/v1/reviews/details?reviewIds[]=4159616459,4162153844,4117852305,4152355291&merchantNo=510159484'
text=requests.get(url).text
# print(text)
# print(type(text))
data=json.loads(text)
# print(type(data))
# a=data[0]
# print(a)
# print(type(a))
# reviewContent=a['reviewContent']
# print(reviewContent)
# reAttatch=a['repThumbnailTagNameDescription']['attachDescription']
# print('-'*50)
# print(reAttatch)

f=open('./Data/review.txt','w',encoding='utf-8')
for a in data:
    reviewContent = a['reviewContent']
    f.write(reviewContent+"\n")
    rep=a['repThumbnailTagNameDescription']
    if rep:
        attach=rep['attachDescription']
        f.write(attach+"\n")

f.close()
print("완료")