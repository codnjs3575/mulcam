from bs4 import BeautifulSoup
import requests

tag = input('search tags :')
url = f'https://www.instagram.com/explore/tags/{tag}'

resp = requests.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
classname = 'KL4Bh'

print(soup.find('div',class_=classname))
bodys = soup.div.parent
print(bodys)
