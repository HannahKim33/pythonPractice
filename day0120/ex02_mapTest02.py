import json
import folium

import pandas as pd

geo_seoul=json.load(open('../Data/EMD_Seoul.geojson', encoding='UTF-8'))

# print(geo_seoul['features'][0]['properties'])
# {'BASE_DATE': '20200630', 'ADM_DR_CD': '1101053', 'ADM_DR_NM': '사직동', 'OBJECTID': '1'}

# print(geo_seoul['features'][0]['geometry'])
# {'type': 'MultiPolygon', 'coordinates': [[[[126.97398562200112, 37.578232670691676], ...

f=pd.read_csv('../Data/Foreigner_EMD_Seoul.csv')
# print(f)
# print(f.info())

# 단계구분도를 만들 때 사용되는 컬럼은 문자열을 상대로 함.
# -> 코드의 자료형을 문자열로 변경해야 함.
f['code']=f['code'].astype(str)
# print(f.info())

# 외국인 인구수에 대한 단계 나누기
bins=list(f['pop'].quantile([0, 0.2, 0.4, 0.6, 0.8, 0.9, 1]))
# print(bins)

# 배경지도 만들기
map_seoul=folium.Map(
    location=[37.56,127],
    zoom_start=12,
    tiles='cartodbpositron'
)

# 단계구분도
folium.Choropleth(
    geo_data=geo_seoul,
    data=f,
    columns = ('code', 'pop'),
    key_on="feature.properties.ADM_DR_CD",
    fill_color="Blues",
    nan_fill_color="White",
    fill_opacity=0.8,
    line_opacity=0.5,
    bins=bins
).add_to(map_seoul)

# 구에 따른 경계선을 추가
# 구의 경계에 대한 geo 데이터를 읽어온다
geo_seoul_sig=json.load(open('../Data/SIG_Seoul.geojson', encoding='UTF-8'))

folium.Choropleth(
    geo_data=geo_seoul_sig,
    fill_opacity=0,
    line_weight=4
).add_to(map_seoul)

#브라우저에서 지도를 출력
# map_seoul.show_in_browser()

# 생성된 단계구분도를 html 파일로 저장
map_seoul.save("../Data/map_seoul.html")
print("단계구분도 html 작성 완료")