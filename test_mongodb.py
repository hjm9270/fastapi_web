from pymongo import MongoClient
import json

# 방법1 - URI
mongodb_URI = "mongodb+srv://root:1234@ubion9.yy3wfaj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongodb_URI)

# 방법2 - HOST, PORT
#client = MongoClient(host='localhost', port=27017)

db = client.ubion9
data = db.mydata
#print(client.list_database_names())

# data.insert_one({
#     "username":"park",
#     "password":"5678"
# })

# cursor = data.find({"username":"kim"})
# print(list(cursor))

cursor_1 = data.find_one({"email":"1@naver.com"})
if cursor_1 == None:
    print("ssssss")
else:
    print(cursor_1)