import requests
import re

# title_replaced=[]
f=open('./Data/startup.txt','w',encoding='utf-8')
for page in range(1,31):
    url='https://kin.naver.com/search/list.naver?query=30%EB%8C%80%20%EC%B0%BD%EC%97%85&page={}'.format(page)
    text=requests.get(url).text
    titles=re.findall(r'<a href=.+?class="_nclicks:kin.txt _searchListTitleAnchor">(.+?)</a>',text)
    for title in titles:
        title=title.replace("<b>","").replace("</b>","")
        # title_replaced.append(title)
        f.write("{}\n".format(title))
f.close()
