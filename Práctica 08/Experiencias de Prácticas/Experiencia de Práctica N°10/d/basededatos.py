#Operacion delete
import sqlite3

conn = sqlite3.connect('pedidos.db')
print("Base de datos abierta satisfactoriamente")
conn.execute("DELETE from ORDERS where ORDERID = 2;")
conn.commit()
print("Número total de registros borrados: ", conn.total_changes)
cursor = conn.execute("SELECT ORDERID, DATE, USERID, TOTAL from ORDERS")
for row in cursor:
    print("ORDERID = ", row[0])
    print("DATE = ", row[1])
    print("USERID = ", row[2])
    print("TOTAL = ", row[3], "\n")
print("Eliminación realizada satisfactoriamente")
conn.close()
