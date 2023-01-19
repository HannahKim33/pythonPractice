import pymongo

url = 'mongodb://127.0.0.1:27017'
dbName='mydb'
client = pymongo.MongoClient(url)
db=client[dbName]
# db.test.insert_one({"x":10,"y":10})
# db.test.insert_one({"x":11,"y":22})
# db.test.insert_one({"x":12,"y":23})

data=db.test.find()
print(data)
print(type(data))

for row in data:
    print(row)