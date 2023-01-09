import json
import re

data='{"ip":"8.8.8.8"}'
print(data,type(data))

#string을 json(dictionary)으로 바꾸기
d1=json.loads(data)
print(d1,type(d1))

#json(dictionary)을 string으로 바꾸기
d2=json.dumps(d1)
print(d2,type(d2))

print("-"*50)

import requests
url='http://www.kma.go.kr/DFSROOT/POINT/DATA/top.json.txt'
text=requests.get(url).text
text=bytes(text,'iso-8859-1').decode('utf-8')
# print(text)

data=json.loads(text)
# print(data[0])
# print(type(data[0]))
#
# print("-"*50)
#
# for row in data:
#     print(row['code'],row['value'])


#정규표현식으로 도시코드와 도시이름을 출력

for row in data:
    str_row=str(row)
    # print(row)
    code=re.findall(r"{'code': '(.+)', 'value': '.+'}",str_row)
    city=re.findall(r"{'code': '.+', 'value': '(.+)'}",str_row)
    print(code[0],city[0])