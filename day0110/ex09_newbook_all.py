#마지막 페이지 번호 가져오기

import requests
from bs4 import BeautifulSoup
import re

url='https://www.hanbit.co.kr/store/books/new_book_list.html'

while True:
    result=requests.get(url)
    bs_obj=BeautifulSoup(result.content,'html.parser')

    paginate=bs_obj.find('div',{'class':'paginate'})
    # print(type(paginate))
    print(paginate)
    a_list=paginate.find_all('a')
    url='https://www.hanbit.co.kr'+a_list[-1]['href']
    print(url)
    num_list=re.findall(r'>(\d+)<',str(paginate))
    print(num_list)

    if '<span>&gt;</span>' not in str(paginate):
        break;

print(num_list[-1])