import requests as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import os
from urllib.request import urlretrieve
import re
import requests as req
from bs4 import BeautifulSoup as bs
from selenium import webdriver  # ✅ 올바른 import 방식
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EC%86%8D%EB%B3%B4")
body=driver.find_element(By.CSS_SELECTOR,"body")
try:
    for i in range(10) :
        body.send_keys(Keys.END)
        time.sleep(0.5)
except:
      print("스크롤완료")
soup = bs(driver.page_source, "lxml")
titleList=[]
title=soup.select("a.news_tit")
for i in title:
    titleList.append(i.text)
dic = {"뉴스제목": titleList}  # ✅ 딕셔너리 형태로 수정
df = pd.DataFrame(dic)
df.to_csv("data.csv", encoding="utf-8-sig", index=False)
