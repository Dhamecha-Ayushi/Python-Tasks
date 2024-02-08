import mysql.connector

conn = mysql.connector.connect(host = "localhost", user = "root", passwd = "root@123", database = "demo")
# print(conn)

cursor = conn.cursor()

# cursor.execute("CREATE DATABASE demo;")
#SHOW DATABASE
# cursor.execute("SHOW DATABASES;")
# for x in cursor:
#     print(x)

#CREATE TABLE
# cursor.execute("CREATE TABLE student(Name Varchar(20), Age int);")
# print("Table Created")

#SHOW TABLES
# cursor.execute("SHOW TABLES;")
# for x in cursor:
#     print(x)

#INSERT QUERY
query = "INSERT INTO student(name, age) VALUES(%s, %d)"
values = [("abc", 22), ("xyz", 24)]
cursor.execute(query, values)

# SELECT QUERY
# cursor.execute("SELECT * FROM student;")
# result = cursor.fetchall()
# for x in result:
#     print(x)

# print(cursor.rowcount, "Row inserted")

#UPDATE QUERY
# cursor.execute("UPDATE student SET age = 25 WHERE name = 'xyz'")
#DELETE QUERY
# cursor.execute("DELETE from student WHERE age = 22")
conn.commit()
conn.close()