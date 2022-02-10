import folium
import json

# 1. starburks01.json 파일을 읽어들기
with open('starburks01.json','r',encoding='utf-8') as f:
    datalist = json.load(f)['store_list']

# 2. 지도 만들기
my_loc = folium.Map(location=[37.623642863177295, 127.07988672065254],zoom_start=16)
folium.Marker([37.623642863177295, 127.07988672065254],
              popup=folium.Popup('우리집', max_width=100),
              icon=folium.Icon(color = 'red',icon='star')
              ).add_to(my_loc)


# 3. starburks01.json 파일 내용(파일 1 실행 결과)을 가지고 반복해서 starburks 매장의 marker를 만들어 지도에 추가하기
for data in datalist :
    folium.Marker([data['lat'], data['lot']],
                  popup=folium.Popup(f'{data["s_name"]} <br> {data["doro_address"]} <br> {data["tel"]}', max_width=300),
                  ).add_to(my_loc)

# 4. 지도 저장하기
my_loc.save('visual03.html')














