import re
import requests

def saveImage(link,title):
    title=title.replace("?","？")
    title=title.replace(":","：")
    f=open('./Webtoon/{}.jpg'.format(title),"wb")
    content=requests.get(link).content
    f.write(content)
    f.close()
    print("{}을 다운받았습니다.".format(title))

url = 'https://comic.naver.com/webtoon/weekday'
tags = requests.get(url).text
# print(tags)
r=re.findall(r'<div class="list_area daily_all">(.+?)<div class="goto_area">',tags,re.DOTALL)
# print(r)
list=re.findall(r'<img onerror=".+?src="(.+?)" width="83".+?title="(.+?)".+?<span class="mask"></span>',r[0],re.DOTALL)
# print(list)
for row in list:
    link,title=row
    saveImage(link,title)

print("모두 다운받았습니다.")

# for i in range(len(img_link)):
#
#     # url='https://shared-comic.pstatic.net/thumb/webtoon/758037/thumbnail/thumbnail_IMAG21_15cb2611-34c0-4f02-a689-41d0b1016579.jpg'
#     data=requests.get(img_link[i]).content
#     f=open('./Data/{}.jpg'.format(title[i]),'wb')
#     f.write(data)
#     f.close()
#     print('파일 생성 완료')