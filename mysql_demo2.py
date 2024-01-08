#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql

# Connect to the database
conn = pymysql.connect(host='localhost', port=3307, user='ai', password='12345678', database='mydatabase')
cursor = conn.cursor()

# Create table
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

# Clear the table
cursor.execute("DELETE FROM users")
conn.commit()

# Insert a record
cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 30)")
conn.commit()

# Query records
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Update a record
cursor.execute("UPDATE users SET age=31 WHERE name='Alice'")
conn.commit()

# Delete a record
cursor.execute("DELETE FROM users WHERE name='Alice'")
conn.commit()

# Close the connection
cursor.close()
conn.close()
