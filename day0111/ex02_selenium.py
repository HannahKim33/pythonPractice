from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import re
import time
import requests
from bs4 import BeautifulSoup

driver=webdriver.Chrome("C:/chromedriver.exe")
driver.get('https://www.python.org/')
# print(driver.title)
time.sleep(5)       #문서를 다 읽기 전에 노드를 찾으면 오류가 날 수 있음. => 대기시간을 주면 됨
elem=driver.find_element(By.NAME, "q")
# print(elem)

# #element의 id가 무엇인지, tag가 무엇인지
# print(elem.get_attribute('id'))
# print(elem.tag_name)

# input 태그 => send_keys
# 클릭 => click
# 현재 보여지는 문서내용 => driver.page_source
# 그다음 원하는 데이터 추출 => re,bs4 
elem.send_keys("pycon"+Keys.ENTER)
time.sleep(1)
html=driver.page_source
print(html)

# while True:
#     pass

driver.close()