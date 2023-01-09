import requests
import re

url='http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
text=requests.get(url).text
# print(text)

# .+    greedy
# .+?   non-greedy
# data=re.findall(r'<location wl_ver="3">.+</location>',text,re.DOTALL)   #DOTALL: 여러 줄에 걸쳐 있을 때
# print(data)
# print(len(data))

location=re.findall(r'<location wl_ver="3">.+?</location>',text,re.DOTALL)   #DOTALL: 여러 줄에 걸쳐 있을 때
# print(data)
# print(len(data))

for row in location:
    # print(row)
    # print("-"*50)
    # province=re.findall(r'<province>(.+)</province>',row)
    # city=re.findall(r'<city>(.+)</city>',row)
    # print(province[0],city[0])
    # date=re.findall(r'<tmEf>(.+)</tmEf>',row)
    # weather=re.findall(r'<wf>(.+)</wf>',row)
    # min=re.findall(r'<tmn>(.+)</tmn>',row)
    # max=re.findall(r'<tmx>(.+)</tmx>',row)
    # for i in range(len(date)):
    #     print(date[i],weather[i],min[i],max[i])
    data=re.findall(r'<data>(.+?)</data>',row,re.DOTALL)
    for day in data:
        item=re.findall(r'<mode>(.+?)</mode>.+?'
					r'<tmEf>(.+?)</tmEf>.+?'
					r'<wf>(.+?)</wf>.+?'
					r'<tmn>(.+?)</tmn>.+?'
					r'<tmx>(.+?)</tmx>.+?'
					r'<rnSt>(.+?)</rnSt>',day,re.DOTALL)

        print(item)