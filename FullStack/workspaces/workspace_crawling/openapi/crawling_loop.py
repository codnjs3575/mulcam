from bs4 import BeautifulSoup
import requests

url = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage=5'

resp = requests.get(url)
soup = BeautifulSoup(resp.text,'html.parser')
pagenums = soup.find_all('nav',{'class':'pagination'})

arr = []
for page in pagenums :
    num = page.find_all('a')
    for i in num :
        arr.append(str(i.text))
arr.pop()
arr.pop()
arr.pop(0)
arr.pop(0)

# nums = list(filter(None, map(lambda x : x.text if x.text.isdigit() else None, pagenums)))


for i in range(1,len(arr)+2):
    print(f'{i}번째 페이지------------------------')
    url = 'https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=FILE&keyword=%EA%B5%90%EC%9C%A1&currentPage='+str(i)

    resp = requests.get(url)
    soup = BeautifulSoup(resp.text,'html.parser')

    datas = soup.find_all('span',{'class':'title'})
    # datas = soup.select('span[class=title]')

    for data in datas :
        title = data.get_text().strip()
        print(title)

















