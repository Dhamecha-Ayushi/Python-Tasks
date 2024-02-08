import sqlite3

conn = sqlite3.connect('sql.db')
cursor = conn.cursor()  #to execute some queries

print('DB Init')

query = 'select sqlite_version();'
cursor.execute(query)
result = cursor.fetchall()
print(f"SqLite version is {result}")

cursor.close()
conn.close()