from hanb_module import getBookInfo
import urllib.request
from bs4 import BeautifulSoup
import json

# url='https://www.hanbit.co.kr/store/books/look.php?p_code=B1068448075'
# print(getBookInfo(url))

url='https://www.hanbit.co.kr/store/books/new_book_list.html'
flag=True
while flag:
    html=urllib.request.urlopen(url)
    bs_obj=BeautifulSoup(html,'html.parser')

    next=bs_obj.find_all('a',{'class':'next'})
    if len(next)!=0:
        url='https://www.hanbit.co.kr'+next[0]['href']
        # print(url)
    else:
        flag=False

paginate=bs_obj.find('div',{'class':'paginate'})
lastPage=''
a_list=paginate.find_all('a')
if len(a_list)==1:
    lastPage=paginate.find('strong').text
else:
    lastPage=a_list[-1].text

lastPage=int(lastPage)

list=[]
# for i in range(1,lastPage+1):
for i in range(1,2):
    url='https://www.hanbit.co.kr/store/books/new_book_list.html?page={}&brand=&cate1=&cate2=&searchKey=&keyWord='.format(i)
    html=urllib.request.urlopen(url)
    bs_obj=BeautifulSoup(html,'html.parser')

    book_tit_list=bs_obj.find_all('p',{'class':'book_tit'})
    for p in book_tit_list:
        url2='https://www.hanbit.co.kr'+p.find('a')['href']
        list.append(getBookInfo(url2))
    print("{} 페이지 수집 완료".format(i))

result={}
result['book_list']=list
# print(result)

# string -> json    :loads()
# json  -> string   :dumps()
data=json.dumps(result)

f=open("./Data/bookinfo.json",'w',encoding="utf-8")
f.write(data)
f.close()