import requests
import re



# url='https://www.hanbit.co.kr/store/books/new_book_list.html'
# text=requests.get(url).text
# flag=True
# while flag:
#     next=re.findall(r'<a href="(.+?)" class="next"><span>&gt;</span></a>',text)
#     print(next)
#     if len(next)==0:
#         flag=False
#     else:
#         url='https://www.hanbit.co.kr{}'.format(next[0])
#         text=requests.get(url).text



f=open("./Data/newbook.csv",'w',encoding='utf-8')

page=1
while True:
    url='https://www.hanbit.co.kr/store/books/new_book_list.html?page=%d&brand=&cate1=&cate2=&searchKey=&keyWord=' %page
    text=requests.get(url).text
    # print(text)
    url_detail=re.findall(r'<p class="book_tit"><a href="(.+)">(.+)</a></p>',text)
    # print(url_detail)
    if bool(url_detail)==False:
        break

    for item in url_detail:
        url2="https://www.hanbit.co.kr%s" %item[0]
        booktitle=item[1]
        booktitle=booktitle.replace('&#40;','(')
        booktitle=booktitle.replace('&#41;',')')
        # print(url2,booktitle)

        detail=requests.get(url2).text

        release_date=re.findall(r'<li><strong>출간 : </strong><span>(.+)</span></li>',detail)
        # print(release_date[0])

        price=re.findall(r'<span class="pbr"><strong>(.+)</strong>원<span>.+</span></span>',detail)
        # print(price[0])

        row="{} {} {}\n".format(booktitle,release_date[0],price[0])
        # print(row)

        f.write(row)

        print("{} 완료".format(booktitle))

    print("{}페이지 완료".format(page))
    page = page+1
f.close()
print("완료")

# <span class="pbr"><strong>24,300</strong>원<span>(10% off)</span></span>
# <p class="book_tit"><a href="/store/books/look.php?p_code=B1147715738">업무에 바로 쓰는 AWS 입문</a></p>
# <ul class="info_list"><li><strong>저자 : </strong><span>김성민 </span></li><li><strong>출간 : </strong><span>2023-01-10</span></li><li><strong>페이지 : </strong><span>360 쪽</span></li><li><strong>ISBN : </strong><span>9791169210652</span></li><li><strong>물류코드 :</strong><span>11065</span></li></ul>