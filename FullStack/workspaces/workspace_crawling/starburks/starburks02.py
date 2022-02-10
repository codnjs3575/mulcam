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
    return gugun_dict


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
    store_list = resp.json()['list']
    data_list = []
    for store in store_list:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['tel'] = store['tel']
        store_dict['doro_address'] = store['doro_address']
        store_dict['lat'] = store['lat']
        store_dict['lot'] = store['lot']
        data_list.append(store_dict)
    return data_list

if __name__ == '__main__':
    # 전국의 모든 스타벅스 매장을 저장
    # all_list = []
    # for key in getSiDo().keys():
    #     for data in getStore(sido_code=key):
    #         all_list.append(data)
    #


    # 강사님 코드
    all_list = list()
    sido_all = getSiDo()
    for sido in sido_all:
        if sido=='17':
            result = getStore(sido_code=sido)
            all_list.extend(result)
            # print(len(result))
        else :
            gugun_all = getGuGun(sido)
            for gugun in gugun_all:
                result = getStore(gugun_code=gugun)
                all_list.extend(result)
    # print(list_all)
    # print(len(list_all))

    # 공통
    all_dict = {}
    all_dict['list'] = all_list

    all_json = json.dumps(all_dict, ensure_ascii=False)
    with open(f'starburks_all.json', 'w', encoding='utf-8') as f:
        f.write(all_json)






