from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import requests
import shutil
import os

# 정보 입력 받기 
hashTag = input("Input a tag to search : ")
scroll_time = int(input("Input scroll times : "))
download_time = int(input("Input download times : "))

# driver load
driver = wd.Chrome(executable_path='/usr/local/bin/chromedriver')
driver.implicitly_wait(5)

# 웹 사이트 접속 # 인스타그램 로그인 URL
loginUrl = 'https://www.instagram.com/accounts/login/'
driver.get(loginUrl)

# 유저 정보 세팅 
username = '' # 아이디
userpw = '' # 패스워드
with open("instagram_user_info.txt", "r") as f:
    username = f.readline()
    userpw = f.readline()

# 로그인 정보 입력
driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_name('password').send_keys(userpw)
driver.find_element_by_name('password').send_keys(Keys.ENTER)
driver.implicitly_wait(5)

# '나중에 하기' 지우기
driver.find_element_by_class_name('aOOlW.HoLwm').click()
driver.implicitly_wait(5)

# 태그 입력, 제일 위 태그 선택 
driver.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input""").send_keys("#" + hashTag)
driver.implicitly_wait(5)
time.sleep(5)
driver.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input""").send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input""").send_keys(Keys.ENTER)
driver.find_element_by_xpath("""//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input""").send_keys(Keys.ENTER)
time.sleep(7)

html = driver.page_source
soup = BeautifulSoup(html, "lxml")

imglist = []

# 이미지 크롤링 with tag
for i in range(0, scroll_time):
    insta = soup.select('.v1Nh3.kIKUG._bz0w')

    for i in insta:
        print('https://www.instagram.com' + i.a['href'])
        imgUrl = i.select_one('.KL4Bh').img['src']
        imglist.append(imgUrl)
        imglist = list(set(imglist))
        html = driver.page_source
        soup = BeautifulSoup(html, "lxml")
        insta = soup.select('.v1Nh3.kIKUG._bz0w')

    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(3)

len_imglist = len(imglist)

# 폴더 생성 
directory = './img/' + hashTag + '/'
if not os.path.exists(directory):
    os.makedirs(directory)

# 이미지 다운로드
n = 0
for i in range(0, download_time):
    if n >= len_imglist:
        break

    image_url = imglist[n]
    resp = requests.get(image_url, stream=True)
    local_file = open(directory + hashTag + str(n) + '.png', 'wb')
    resp.raw.decode_content = True
    shutil.copyfileobj(resp.raw, local_file)

    n += 1
    del resp

driver.close()
