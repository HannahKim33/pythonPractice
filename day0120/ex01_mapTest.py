import json
import pandas as pd

#시, 군 , 구 경계 지도 데이터 읽어들이기
geo=json.load(open('../Data/SIG.geojson',encoding='UTF-8'))

#행정구역 코드
# print(geo['features'][0]['properties'])
# {'SIG_CD': '42110', 'SIG_ENG_NM': 'Chuncheon-si', 'SIG_KOR_NM': '춘천시'}

#위도, 경도
# print(geo['features'][0]['geometry'])
#{'type': 'MultiPolygon', 'coordinates': [[[[127.58508551154958, 38.08062321552708],
# ... , [127.58508551154958, 38.08062321552708]]]]}

#시군구별 인구 데이터 준비하기
df_pop=pd.read_csv('../Data/Population_SIG.csv')
# print(df_pop.head())

# print(df_pop.info())

# code를 문자열로 변환
df_pop['code']=df_pop['code'].astype('str')
# print(df_pop.info())

# 지도위에 지역별로 구분하여 그림을 그리는 것을 "단계구분도"라고 합니다.
# 지도위에 지역별로 구분하여 그 지역의 인구수에 따라 색상을 다르게 표현하려고 합니다.

# 배경지도 만들기
import folium
# map=folium.map(
#     location=[35.95, 127.7],
#     zoom_start=8
# )

# 지도를 브라우저에 보여주기
# map.show_in_browser();

# 기본적으로 만들어지는 지도배경은 색칠되어 그려진다.
# 단계구분도를 위해서는 색칠되지 않은 배경의 지도를 만들어야 함.

map_sig=folium.Map(
    location=[35.95, 127.7],
    zoom_start=8,
    tiles="cartodbpositron"
)

# folium.Choropleth(
#     geo_data=geo,
#     data=df_pop,
#     columns=('code','pop'),
#     key_on="feature.properties.SIG_CD"
# ).add_to(map_sig)

# 준비된 통계데이터의 인구수 pop의 최소값부터 최대값까지를 몇 개의 단계로 나누어 봅니다.
bins=list(df_pop['pop'].quantile([0,0.2,0.4,0.6,0.8,1]))
print(bins)
# [8867.0, 50539.6, 142382.20000000004, 266978.6, 423107.20000000024, 13565450.0]

# 위에서 나눈 단계에 따라서 단계 구분도를 다시 만들어 봅시다.

folium.Choropleth(
    geo_data=geo,
    data=df_pop,
    columns=('code','pop'),
    key_on='feature.properties.SIG_CD',
    fill_color="Blues",
    fill_opacity=1,
    line_opacity=0.5,
    bins=bins
).add_to(map_sig)

map_sig.show_in_browser()