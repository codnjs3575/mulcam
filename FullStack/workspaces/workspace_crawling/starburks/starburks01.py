# -*- coding:utf-8 -*-

import requests
import json

def getSiDo():
    url = 'https://www.starbucks.co.kr/store/getSidoList.do' # 가지고 오려는 endpoint (root + service)
    resp = requests.post(url) # __ajaxCall('/store/getSidoList.do", {},true,'json','post'
    datas = resp.json()['list'] # .json() : requests의 기능
    sido_code = []
    sido_nm = []
    for data in datas :
        sido_code.append(data["sido_cd"])
        sido_nm.append(data["sido_nm"])

    # 강사님 코드
    # sido_code = list(map(lambda x: x['sido_cd'],datas))
    # sido_nm = list(map(lambda x: x['sido_nm'], datas))

    sido_dict = dict(zip(sido_code,sido_nm))
    return sido_dict

def getGuGun(sido_code):
    url = 'https://www.starbucks.co.kr/store/getGugunList.do'
    data_dict = {"sido_cd" : sido_code}
    resp = requests.post(url,data_dict)
    datas = resp.json()['list']

    gugun_code = []
    gugun_nm = []

    for data in datas:
        gugun_code.append(data['gugun_cd'])
        gugun_nm.append(data['gugun_nm'])
    gugun_dict = dict(zip(gugun_code, gugun_nm))
    # print(gugun_dict)
    return gugun_dict

    # 강사님 코드
    # gugun_dict = dict(zip(list(map(lambda x:x['gugun_cd'],datas)),
    #                       list(map(lambda x:x['gugun_nm'],datas))))

def getStore(sido_code = '',gugun_code=''):
    # var storeInterfaceUrl = "/store/getStore.do?r="+rndCod;
    # __ajaxCall( storeInterfaceUrl ,$search, true, "json", "post",
    url = 'https://www.starbucks.co.kr/store/getStore.do'
    resp = requests.post(url,data={"ins_lat": "37.6242176",
                                   "ins_lng": "127.0710272",
                                   "p_sido_cd": sido_code,
                                   "p_gugun_cd": gugun_code,
                                   "in_biz_cd": '',
                                   "set_date":'',})
    # print(resp.json())
    store_list = resp.json()['list']
    data_list = []
    data_dict = {}
    for store in store_list:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['tel'] = store['tel']
        store_dict['doro_address'] = store['doro_address']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']
        data_list.append(store_dict)
    data_dict['store_list'] = data_list
    res_json = json.dumps(data_dict, ensure_ascii=False)

    global sido_name
    with open(f'starburks_{sido_name}.json', 'w', encoding='utf-8') as f:
        f.write(res_json)

    return data_dict

if __name__ == '__main__':
    getsido = getSiDo()
    sido = input('도시 코드 입력 :')
    sido_name = getsido[sido]

    if sido == '17' :
        print(getStore(sido_code='17',gugun_code=''))
    else :
        print(getGuGun(sido))
        gugun = input('구군 코드 입력 :')
        print(getStore(gugun_code=gugun))

