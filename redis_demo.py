#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import redis

# 连接数据库
r = redis.Redis(host='localhost', port=6379, db=0)

# 清空数据库
r.flushdb()

# 增加
r.set('name', 'Alice')

# 查询
print(r.get('name'))

# 更新
r.set('name', 'Bob')

# 删除
r.delete('name')
