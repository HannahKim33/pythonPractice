import json
geo=json.load(open('../Data/SIG.geojson', encoding='UTF-8'))
# print(geo.keys())
# dict_keys(['type', 'name', 'crs', 'features'])
# print(geo['type'])
# print(type(geo['type']))
# # FeatureCollection
# # <class 'str'>
# print(geo['name'])  #sig
# print(geo['crs'])
f=geo['features']
# print(f)
# print(type(f))
# print(len(f))
# print(f[0])
keylist=f[0].keys()
# print(keylist)
# dict_keys(['type', 'properties', 'geometry'])
# print(f[0]['type'])     #Feature
# print(f[0]['properties'])   #{'SIG_CD': '42110', 'SIG_ENG_NM': 'Chuncheon-si', 'SIG_KOR_NM': '춘천시'}
# print(f[0]['geometry'])     #keys: 'type', 'coordinates'
print(f[0]['geometry']['coordinates'])      #4차원 배열. 위도 경도 정보