#style-scope yt-formatted-string
import bs4
import urllib.request

# url='https://stackoverflow.com/questions'
# html=urllib.request.urlopen(url)
# bs_obj=bs4.BeautifulSoup(html,'html.parser')
# spans=bs_obj.find_all('a',{'class':'s-link'})
# # print(bs_obj)
# print(spans)
str=''
page=1
while True:
    url='https://www.seek.com.au/jobs-in-information-communication-technology/developers-programmers?page={}'.format(page)
    html=urllib.request.urlopen(url)
    bs_obj=bs4.BeautifulSoup(html,'html.parser')
    spans=bs_obj.find_all('span',{'data-automation':'jobShortDescription'})
    # print(bs_obj)
    # print(spans)
    for span in spans:
        str+=span.text
    page=page+1
    if page>50:
        break;

print(str)
str_split=str.split()