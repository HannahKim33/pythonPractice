import pymongo

url = 'mongodb://127.0.0.1:27017';
dbName = 'mydb';
colName = "member"
client = pymongo.MongoClient(url)
db = client[dbName]

#다큐먼트를 추가 하는 함수
def insertMember(doc):
    db[colName].insert_one(doc)

#모든 다큐먼트를 조회하여 반환하는 함수
def listMember():
    print("함수동작함.")
    list =  db[colName].find()
    # print(list)
    # for row in list:
    #     print(row)
    return list
