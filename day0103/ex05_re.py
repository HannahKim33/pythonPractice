import requests
import re

# url='https://www.hanbit.co.kr/'
# text=requests.get(url).text
# # print(text)
# title=re.findall(r'<a href="https://www.hanbit.co.kr/index.html">(.+)</a>',text)    #findAll은 list를 반환함
# print(title)
# print(title[0])

# url='http://mpllc-seat.sen.go.kr/seatinfo/Seat_Info/1_count.asp'
# text=requests.get(url).text
# seats=re.findall(r'<td class="wating_f">(.+)</td>',text)
# print(seats[0])
# n=int(seats[0])
# print(n)

#<span id="Layer110" style="position:absolute; left:251px; top:55; width:30px; height:25px; z-index:1; background-color: #FFFE91; border: 1px solid #000000;"><table height="100%" align="center" valign="middle"  cellpadding="0" cellspacing="0" style="margin:0px"><tr><td><font size ="2">2</td></tr></table></span>

url='http://mpllc-seat.sen.go.kr/seatinfo/Seat_Info/1_readingroom.asp'
text=requests.get(url).text
# print(text)
data=re.findall(r'<span id="Layer110".+#FFFE91;.+<font size ="2">(.+)</td></tr></table></span>',text)
print(data)