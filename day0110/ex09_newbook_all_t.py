import urllib.request
from bs4 import BeautifulSoup
import re

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

for i in range(1,lastPage+1):
    url='https://www.hanbit.co.kr/store/books/new_book_list.html?page={}&brand=&cate1=&cate2=&searchKey=&keyWord='.format(i)
    html=urllib.request.urlopen(url)
    bs_obj=BeautifulSoup(html,'html.parser')

    book_tit_list=bs_obj.find_all('p',{'class':'book_tit'})
    for title in book_tit_list:
        print(title.text)