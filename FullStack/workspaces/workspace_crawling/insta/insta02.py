from selenium import webdriver
from bs4 import BeautifulSoup

tag = input('search tags :')
url = f'https://www.instagram.com/explore/tags/{tag}'

service = webdriver.chrome.service.Service('../drivers/chromedriver')
driver = webdriver.Chrome(service=service) # Chrome 객체 생성

driver.implicitly_wait(3) # 3초 기다린 후,
driver.get(url) # url 가져오기

soup = BeautifulSoup(driver.page_source, 'html.parser')
img_list = soup.find_all('div',class_='KL4Bh')

for img in img_list :
    print(img)











