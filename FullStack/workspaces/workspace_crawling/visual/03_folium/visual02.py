import folium

my_loc = folium.Map(location=[37.623642863177295, 127.07988672065254],zoom_start=18) # 10 ~ 18
folium.Marker([37.623642863177295, 127.07988672065254],popup=folium.Popup('우리집',max_width=100)).add_to(my_loc)

my_loc.save('visual02.html')
