import requests
import re

# title_replaced=[]
# f=open('./Data/startup2.txt','w',encoding='utf-8')
for page in range(1,31):
    url='https://kin.naver.com/search/list.naver?query=30%EB%8C%80%20%EC%B0%BD%EC%97%85&page={}'.format(page)
    text=requests.get(url).text
    items=re.findall(r'<a href="(.+?)".+?class="_nclicks:kin.txt _searchListTitleAnchor">(.+?)</a>',text)
    # print(items)
    for i in range(len(items)):
        titleUrl=items[i][0]
        detail=requests.get(titleUrl).text
        contents=re.findall(r'<div class="c-heading__content">(.+?)</div>',detail,re.DOTALL)
        for content in contents:
            content=content.replace("<p>","").replace("</p>","").replace("&nbsp;","")
            print(content)