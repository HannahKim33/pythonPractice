from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from bs4 import BeautifulSoup
import pandas as pd
import requests

url='https://smartstore.naver.com/wenximall/products/3662937494?n_media=11068&n_rank=2&n_ad_group=grp-a001-02-000000029466340&n_ad=nad-a001-02-000000203980487&n_campaign_type=2&n_mall_id=ncp_1nlk5y_01&n_mall_pid=3662937494&n_ad_group_type=2&NaPm=ct%3Dlcpzcqbs%7Cci%3D0zm0003r8VPx7omLaflo%7Ctr%3Dpla%7Chk%3D841162f2c691c32210d3e3a55ac6daf487f2e47d'
# wd = webdriver.Chrome('./WebDriver/chromedriver.exe')
#
# result = []
# for i in range(1, 5):
#     try:
#         wd.get(url)
#         element = WebDriverWait(wd, 2).until(
#             expected_conditions.presence_of_element_located((By.CLASS_NAME, "store_table")))
#         html = wd.page_source
#         soup = BeautifulSoup(html, 'html.parser')
#         print(soup)
#     except:
#         print(f'{i} : not exist')
#         continue
# wd.quit()
# df = pd.DataFrame(result, columns = ('name', 'address', 'phone'))
# df.to_csv('./Data/review.txt', encoding='utf-8', mode='w', index=False)
# print('Completed..')


# f=open("./Data/review.txt",'w',encoding='utf-8')

result=requests.get(url)
bs_obj=BeautifulSoup(result.content,'html.parser')

print(bs_obj)
span_list=bs_obj.find_all('span',{'class':'_3QDEeS6NLn'})

# print(span_list)