from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

input_id = input('id :')
input_pw = input('pw :')

service = webdriver.chrome.service.Service('../drivers/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get('https://www.instagram.com/accounts/login/')
sleep(5)

# id input 찾기
id = driver.find_element(By.NAME, 'username')
id.send_keys(input_id)

# pw input 찾기
pw = driver.find_element(By.NAME, 'password')
pw.send_keys(input_pw)
sleep(2)

# 로그인 버튼 클릭하기
driver.find_element(By.CSS_SELECTOR,'#loginForm>div>div:nth-child(3)').click()
sleep(3)
driver.refresh()
sleep(3)

later = driver.find_element(By.XPATH,'/html/body/div[1]/section/main/div/div/div/div/button')
later.click()
sleep(3)

later2 = driver.find_element(By.XPATH,'/html/body/div[6]/div/div/div/div[3]/button[2]')
later2.click()
sleep(3)