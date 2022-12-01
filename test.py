import mysql.connector
from mysql.connector import errorcode

mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "soh"
        )
ptr  = mydb.cursor(buffered=True)
query = f"select id from test order by id desc"
ptr.execute(query)
a = ptr.fetchall()
print(a[0])

mydb.commit()
mydb.close()

