import json
import pandas as pd

geo=json.load(open('../Data/SIG.geojson', encoding='UTF-8'))
df_pop=pd.read_csv('../Data/Population_SIG.csv')
# print(df_pop.head())
# print(df_pop.info())

df_pop['code']=df_pop['code'].astype(str)
# print(df_pop.info())

import folium

# map1 = folium.Map(location=[35.95, 127.7], zoom_start=20)
# map1.show_in_browser()  # 지도를 브라우저에 출력

map_sig=folium.Map(location=[35.95, 127.7],
                   zoom_start=8,
                   tiles='cartodbpositron')

# folium.Choropleth(
#     geo_data=geo,
#     data=df_pop,
#     columns=('code','pop'),
#     key_on='feature.properties.SIG_CD').add_to(map_sig)

bins=list(df_pop['pop'].quantile([0,0.2,0.4,0.6,0.8,1]))

folium.Choropleth(
    geo_data=geo,
    data=df_pop,
    columns=('code','pop'),
    key_on='feature.properties.SIG_CD',
    bins=bins,
    fill_color='Blues',
    fill_opacity=1,
    line_opacity=0.5
).add_to(map_sig)

map_sig.show_in_browser()