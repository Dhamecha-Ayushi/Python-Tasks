import pandas as pd
import os
import sys
import re
import mysql.connector

conn = mysql.connector.connect(host = "localhost", user = "root", password = "root@123", database = "mydb")

cur = conn.cursor()
file = "ping_links.xlsx"
data = pd.read_excel(file, engine="openpyxl")

dict1 ={}
for i in data.values:
    # print(i)
    dict1[i[0]] = i[1]
# print(dict1)    
ip_name = dict1.keys()
ip = dict1.values()
for i in ip:
    res = os.popen(f"ping -c 5 {i}").read()
    # print(res)
    temp = res.splitlines()
    # print(temp[-1])
    temp2 = temp[-1]
    val = re.split(r"[/=\s+]", temp2)

    # import pdb; pdb.set_trace()
    min_val = val[7]
    max_val = val[9]
    avg_val = val[8]
    # import pdb; pdb.set_trace()
    mi = float(min_val)
    ma = float(max_val)
    av = float(avg_val)
    # for i in val:
    #     min1 = i
    
    # import pdb; pdb.set_trace()
    # print(f"min:{min_val}, max:{max_val}, avg:{avg_val}")
    query = "INSERT INTO store_ping(name, min_value, max_value, average) VALUES(%s, %s, %s, %s)"
    for i in ip_name:
        import pdb; pdb.set_trace()
        values = [i, mi, ma, av]
        cur.execute(query,values)

    conn.commit()    
    # dic = {(x,y) for x in val for y in val if }
cur.close()
conn.close()
    # print(val)
