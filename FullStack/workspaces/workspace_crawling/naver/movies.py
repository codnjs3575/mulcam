from bs4 import BeautifulSoup
import urllib.request

resp = urllib.request.urlopen('https://movie.naver.com/movie/running/current.naver')
# print(resp) # document

soup = BeautifulSoup(resp,'html.parser') # 객체 : <class 'bs4.BeautifulSoup'>
# print(type(soup))

movies = soup.find_all('dl',class_='lst_dsc')
# print(movies[0])

for movie in movies :
    # 제목
    title = movie.find('a').get_text()

    # 별점
    star = movie.find('span',class_='num').text
    print(f'{title} {star}')