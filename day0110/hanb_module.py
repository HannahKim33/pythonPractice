import urllib.request
from bs4 import BeautifulSoup

def getBookInfo(url):
    html = urllib.request.urlopen(url)
    bs_obj = BeautifulSoup(html, 'html.parser')
    box = bs_obj.find('div', {'class': 'store_product_info_box'})

    title = box.find('h3').text
    price = bs_obj.find('span', {'class': 'pbr'}).find('del').text

    info_list = box.find('ul', {'class': 'info_list'})
    lis = info_list.find_all('li')

    for li in lis:
        strong = li.find('strong').text
        if '저자' in strong:
            author = li.find('span').text
        elif '출간' in strong:
            reldate = li.find('span').text
        elif '페이지' in strong:
            pages = li.find('span').text

    return {'title':title, 'price':price, 'author':author, 'reldate':reldate, 'pages':pages}