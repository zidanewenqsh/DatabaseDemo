#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pymongo import MongoClient

# 连接数据库
client = MongoClient('mongodb://localhost:27017/')
db = client['test_db']

# 清空集合
db['users'].delete_many({})

# 增加
db['users'].insert_one({'name': 'Alice', 'age': 30})

# 查询
print(list(db['users'].find()))

# 更新
db['users'].update_one({'name': 'Alice'}, {'$set': {'age': 31}})

# 删除
db['users'].delete_one({'name': 'Alice'})
