# -*- coding:utf-8 -*-

import requests
import json


def getSiDo():
    # __ajaxCall("/store/getSidoList.do", {}, true, "json", "post",
    url = 'https://www.starbucks.co.kr/store/getSidoList.do'
    # 엔드포인트 = root 라고 생각하면 편함. 딱 기본서버 url임
    resp = requests.post(url)
    #print(resp)
    #print(resp.json())   # 응답받은 데이터를 json 객체로 바꿔줌 => requests 모듈의 기능

    sido_list = resp.json()['list']   # 리스트라는 키를 주면 그 value값이 나올 것
    #print(sido_list[3])

    sido_code = list(map(lambda x : x['sido_cd'], sido_list))
    sido_nm = list(map(lambda x : x['sido_nm'], sido_list))
    #print(sido_code)
    #print(sido_nm)

    sido_dict = dict(zip(sido_code, sido_nm))
    #print(sido_dict)

    return sido_dict

def getGuGun(sido_code):
    # __ajaxCall("/store/getGugunList.do", {"sido_cd":sido}, true, "json", "post",
    url = 'https://www.starbucks.co.kr/store/getGugunList.do'
    resp = requests.post(url, data={'sido_cd': sido_code})
    gugun_list = resp.json()['list']
    gugun_dict = dict(zip(list(map(lambda x: x['gugun_cd'], gugun_list)),
                list(map(lambda x:x['gugun_nm'], gugun_list))))
    return gugun_dict

def getStore(sido_code='', gugun_code=''):
    url = 'https://www.starbucks.co.kr/store/getStore.do'
    resp = requests.post(url, data={"ins_lat": "37.502976",
                                     "ins_lng": "126.97865",
                                     "p_sido_cd": sido_code,
                                     "p_gugun_cd": gugun_code,
                                     "in_biz_cd": '',
                                     "set_date":''})
    store_list = resp.json()['list']
    # s_name, tel, doro_address, lat, lot
    result_list = list()
    for store in store_list:
        store_dict = dict()
        store_dict['s_name'] = store['s_name']
        store_dict['tel'] = store['tel']
        store_dict['doro_address'] = store['doro_address']
        store_dict['let'] = store['lat']
        store_dict['lot'] = store['lot']
        result_list.append(store_dict)

    return result_list

if __name__ == "__main__":
    # 전국의 모든 스타벅스 매장을 저장
    # {'list' : [{s_name:'',..}, {}, ...]}
    # starbucks_all.json
    list_all = list()

    sido_all = getSiDo()
    for sido in sido_all:
        if sido == '17':
            result = getStore(sido_code=sido)
            print(result)
            list_all.extend(result)
        else:
            gugun_all = getGuGun(sido)
            for gugun in gugun_all :
                result = getStore(gugun_code=gugun)
                print(result)
                list_all.extend(result)

    #print(list_all)
    #print(len(list_all))

    result_dict = dict()
    result_dict['list'] = list_all

    result = json.dumps(result_dict, ensure_ascii=False)
    with open('starbucks_all.json', 'w', encoding='utf-8') as f:
        f.write(result)