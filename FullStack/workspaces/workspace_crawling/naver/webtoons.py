# -*-  coding : utf-8 -*-
# 해당 py파일은 utf-8로 인코딩 됨

from bs4 import BeautifulSoup
import requests
import json

url = 'https://comic.naver.com/webtoon/weekdayList?week=wed'

resp = requests.get(url) #get방식으로 해당 url에 요청
# print(resp)
# print(resp.text) # 문자열

soup = BeautifulSoup(resp.text,'html.parser')
# print(soup) # 객체

webtoons = soup.find('ul', {'class': 'img_list'});

dl_list = webtoons.select('dl')
lst = list()

for dl in dl_list:
    # print(dl)
    title = dl.find('a')['title']
    star = dl.find('strong').text

    tmp = dict()
    tmp['title'] = title
    tmp['star'] = star
    lst.append(tmp)

# print(lst)
res = dict()
res['webtoons'] = lst
# print(res)
res_json = json.dumps(res, ensure_ascii=False)
print(res_json)

with open('webtoons.json','w',encoding='utf-8') as f :
    f.write(res_json)








