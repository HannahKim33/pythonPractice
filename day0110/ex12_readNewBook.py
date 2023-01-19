import json

import pandas

f=open("./Data/bookinfo.json",'r',encoding='utf-8')

line=f.readline()
data=json.loads(line)
# print(data)
book_list=data['book_list']
print(book_list)
print(type(book_list))
# for book in book_list:
#     print(book)
# f.close()


# df=pandas.read_json("./Data/bookinfo.json")
# print(df)

