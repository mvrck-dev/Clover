from operator import truediv
import random
import mysql.connector as dbcn

# Initialising Database
activedb = dbcn.connect(host = "localhost", user = "root", password= "destiny012", database = "test")

cur = activedb.cursor()

uid = random.randint(0, 99999)

cur.execute(f"SELECT userid FROM test1")
uidchk = cur.fetchall()

for i in uidchk:
    if uid in i:
        uid = random.randint(0, 99999)
    else:
        break

cur.execute(f"SELECT * FROM test1")
print(cur.fetchall())