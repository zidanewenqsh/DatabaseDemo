#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from neo4j import GraphDatabase

# 连接数据库
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

# 清空数据库
with driver.session() as session:
    session.run("MATCH (n) DETACH DELETE n")

# 增加
with driver.session() as session:
    session.run("CREATE (a:Person {name: 'Alice', age: 30})")

# 查询
with driver.session() as session:
    result = session.run("MATCH (a:Person) RETURN a.name, a.age")
    for record in result:
        print(record)

# 更新
with driver.session() as session:
    session.run("MATCH (a:Person {name: 'Alice'}) SET a.age = 31")

# 删除
with driver.session() as session:
    session.run("MATCH (a:Person {name: 'Alice'}) DELETE a")

# 关闭连接
driver.close()

