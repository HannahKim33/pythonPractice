import urllib.request
import bs4

url='https://www.hanbit.co.kr/store/books/new_book_list.html'
html=urllib.request.urlopen(url)

bs_obj=bs4.BeautifulSoup(html,'html.parser')
p_list=bs_obj.find_all('p',{'class':'book_tit'})
for p in p_list:
    print(p.find('a').text)