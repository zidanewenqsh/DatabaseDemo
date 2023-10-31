#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from neo4j import GraphDatabase

# 初始化数据库连接
driver = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))

# 清空整个数据库
def clear_database(tx):
    tx.run("MATCH (n) DETACH DELETE n")

# 创建节点和边
def create_node_and_relationship(tx):
    tx.run("CREATE (a:Person {name: 'Alice', age: 25})-[:KNOWS]->(b:Person {name: 'Bob', age: 30})")

# 查询节点
def query_node(tx):
    result = tx.run("MATCH (a:Person) WHERE a.name = 'Alice' RETURN a.name, a.age")
    for record in result:
        print(record)

# 更新节点属性
def update_node(tx):
    tx.run("MATCH (a:Person {name: 'Alice'}) SET a.age = 26")

# 删除节点（同时删除与其相关的边）
def delete_node(tx):
    tx.run("MATCH (a:Person {name: 'Alice'}) DETACH DELETE a")

# 创建边
def create_relationship(tx):
    tx.run("MATCH (a:Person), (b:Person) WHERE a.name = 'Alice' AND b.name = 'Bob' CREATE (a)-[:FRIENDS_WITH]->(b)")

# 删除边
def delete_relationship(tx):
    tx.run("MATCH (a:Person)-[r:FRIENDS_WITH]->(b:Person) WHERE a.name = 'Alice' AND b.name = 'Bob' DELETE r")

# 执行操作
with driver.session() as session:
    session.execute_write(clear_database)  # 清空数据库
    session.execute_write(create_node_and_relationship)
    session.execute_read(query_node)
    session.execute_write(update_node)
    session.execute_write(create_relationship)
    session.execute_write(delete_relationship)
    session.execute_write(delete_node)

# 关闭数据库连接
driver.close()
