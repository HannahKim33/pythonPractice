import requests
import re
url='http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
text=requests.get(url).text
# print(text)


location_list=re.findall(r'<location wl_ver="3">.+?</location>',text,re.DOTALL)
# print(location)

f=open('./Data/kma.txt','w',encoding='utf-8')
# 내가 한 거
# for row in location_list:
#     # print(row)
#     city=re.findall(r'<city>(.+)</city>',row)
#     date=re.findall(r'<tmEf>(.+)</tmEf>',row)
#     wf=re.findall(r'<wf>(.+)</wf>',row)
#     tmn=re.findall(r'<tmn>(.+)</tmn>',row)
#     tmx=re.findall(r'<tmx>(.+)</tmx>',row)
#     print(city[0])
#     f.write(city[0])
#     for i in range(len(date)):
#         print(date[i],wf[i],tmn[i],tmx[i])
#         f.write("{0} {1} {2} {3} \n".format(date[i],wf[i],tmn[i],tmx[i]))

#선생님이 한 거
for location in location_list:
    # print(row)
    city=re.findall(r'<city>(.+)</city>',location)
    data_list=re.findall(r'<data>(.+?)</data>',location,re.DOTALL)

    for data in data_list:
        date = re.findall(r'<tmEf>(.+)</tmEf>', data)
        wf=re.findall(r'<wf>(.+)</wf>',data)
        tmn=re.findall(r'<tmn>(.+)</tmn>',data)
        tmx=re.findall(r'<tmx>(.+)</tmx>',data)
        # print(city[0],date[0],wf[0],tmn[0],tmx[0])
        # row="%s,%s,%s,%s,%s \n" %(city[0],date[0],wf[0],tmn[0],tmx[0])
        row="{},{},{},{},{}\n".format(city[0],date[0],wf[0],tmn[0],tmx[0])
        f.write(row)
    print("%s의 내용을 기록했습니다." %city)

f.close()
print("모두 출력 완료")
