import pymongo

url = 'mongodb://127.0.0.1:27017'
dbName='mydb'
collectionName="member"
client = pymongo.MongoClient(url)
db=client[dbName]

def insertMember(doc):
    db[collectionName].insert_one(doc)

def listMember():
    return db[collectionName].find()