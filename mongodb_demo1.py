#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

# 连接到 MongoDB
client = MongoClient('mongodb://localhost:27017/')

# 选择或创建数据库
db = client['my_database']

# 获取所有集合名称
collection_names = db.list_collection_names()

# 删除所有集合
for name in collection_names:
    db.drop_collection(name)

print("所有集合已删除。")

collection = db.my_collection
document = {"name": "John", "age": 30, "city": "New York"}
collection.insert_one(document)
documents = [
    {"name": "Tom", "age": 33, "city": "New York"},
    {"name": "Marie", "age": 22, "city": "Boston"},
    {"name": "Mike", "age": 32, "city": "Chicago"}
]
collection.insert_many(documents)
query = {"name": "John"}
result = collection.find_one(query)
print(result)
results = collection.find({"age": {"$gt": 25}})
for result in results:
    print(result)

update_query = {"name": "John"}
new_values = {"$set": {"age": 40}}

collection.update_one(update_query, new_values)

delete_query = {"name": "John"}
collection.delete_one(delete_query)
client.close()
