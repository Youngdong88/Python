import pandas as pd
import numpy as np
import seaborn as sns
%matplotlib notebook
import matplotlib.pyplot as plt
import googlemaps
gmaps_key = "AIzaSyDaxET0a61q9RVl8GXHajDiYONxSwpkSt8"
gmaps = googlemaps.Client(key = gmaps_key)

crime_seoul = pd.read_csv("crime_Seoul2.csv", encoding = "utf-8",
                         index_col = 0)

#
crime_seoul['관서명']
stations1 = []
for name in crime_seoul['관서명'] :
    stations1.append('서울' + name[:-1] + '경찰서') # 서울OO경찰서로 바꿔주려고

a = []
for i in range(0, 30):
    a.append(stations2[i][0]["geometry"]["location"]["lat"])

b = []
for i in range(0, 30):
    b.append(stations2[i][0]["geometry"]["location"]["lng"])

fm = folium.Map(location =(37.5, 127))
for i in range(0, 30):
    folium.Marker([a[i], b[i]], popup = stations1[i], icon = folium.Icon(icon = "cloud")).add_to(fm)
fm
