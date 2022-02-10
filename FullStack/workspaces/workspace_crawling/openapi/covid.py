from xml.etree import ElementTree
import requests
import re

service_key='VXBYQ69L5Fwe5N6ROU%2BQDFRw2QT7VAQq2iW9WUSFjTxT5tCatN27CjwGwFKDLtqMhSaBV2BfjIAhytbw2lcWmg%3D%3D'
# service_key ='KP77evFWYDuFWsIWM%2FzvBJbp8ttP2uLl5sh7hOYoKWzv4ZlCus8FGs13a15cmo2V%2B%2FK6p92nhpXG8B0iXVuqiA%3D%3D'
url = f'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?ServiceKey={service_key}'
# print(url)

resp = requests.get(url)
# print(resp.text)
tree = ElementTree.fromstring(resp.text) # resp.text(문자열)가지고 xml paesetree 생성

for item in tree[1][0]:
    gubun = item.find('gubun').text
    # print(gubun)
    if gubun == '합계':
        # print(f'{item.find("stdDay").text}')
        stdday = item.find("stdDay").text
        print(f'[{stdday[2:4]}/{stdday[6:8]}/{stdday[10:12]}]')
        # stdday = re.sub(r'(\D)+','',stdday)
        # stdday = stdday[2:4]+'/'+stdday[4:6]+'/'+stdday[6:8]
        # print(stdday)
        print(f'일일합계 : {item.find("localOccCnt").text }')
        print(f'국내발생 : {item.find("incDec").text }')
        print(f'해외발생 : {item.find("overFlowCnt").text }')
















