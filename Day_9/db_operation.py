import sqlite3

conn = sqlite3.connect('sql.db')
cursor = conn.cursor()

cursor.execute('create table employee(name, age)')
values = [('Ayushi', 22), ('Jenil', 21)]

# cursor.execute("insert into employee values ('Dhruv', 25)")
cursor.executemany("insert into employee values (?,?)", values)
res = cursor.execute('select * from employee')
print(cursor.rowcount, "record inserted")
print(list(res))
# cursor.execute('DROP table employee')
conn.commit()
cursor.close()
conn.close()