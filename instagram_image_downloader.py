from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import quote_plus
from urllib.request import urlopen
import time
import requests
import shutil
from icecream import ic

# import pandas_csv

baseUrl = "https://www.instagram.com/explore/tags/"
plusUrl = input("Input a tag to search : ")
url = baseUrl + quote_plus(plusUrl)
scroll_time = int(input("Input scroll times : "))
download_time = int(input("Input download times : "))

driver = webdriver.Chrome()
driver.get(url)

time.sleep(3)

email = ""
password = ""
with open("instagram_user_info.txt", "r") as f:
    email = f.readline()
    password = f.readline()

input_id = driver.find_element_by_css_selector("input._2hvTZ.pexuQ.zyHYP")[0]
input_id.clear()
input_id.send_keys(email)

input_pw = driver.find_element_by_css_selector("input._2hvTZ.pexuQ.zyHYP")[0]
input_pw.clear()
input_pw.send_keys(password)
input_pw.submit()

html = driver.page_source
soup = BeautifulSoup(html)

imglist = []

for i in range(0, scroll_time):
    insta = soup.select('.vlNh3.kIKUG._bz0w')

    for i in insta:
        print("https://www.instagram.com" + i.a["href"])
        imgUrl = i.select_one(".KL4Bh").img["src"]
        imglist.append(imgUrl)
        imglist = list(set(imglist))
        html = driver.page_source
        soup = BeautifulSoup(html)
        insta = soup.select('.vlNh3.kIKUG._bz0w')

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

n = 0

for i in range(0, download_time):
    image_url = imglist[n]
    resp = requests.get(image_url, stream=True)
    local_file = open("./img/" + plusUrl + str(n) + ".jpg", "wb")
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)
    n += 1
    del resp

driver.close()


