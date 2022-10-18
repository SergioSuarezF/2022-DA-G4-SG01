#Operacion actualizar
import sqlite3

conn = sqlite3.connect('pedidos.db')
print("Base de datos abierta satisfactoriamente")
conn.execute("UPDATE ORDERS set TOTAL = 25000.00 where ORDERID = 1")
conn.commit()
print("Número total de registros actualizados: ", conn.total_changes)
cursor = conn.execute("SELECT ORDERID, DATE, USERID, TOTAL from ORDERS")
for row in cursor:
    print("ORDERID = ", row[0])
    print("DATE = ", row[1])
    print("USERID = ", row[2])
    print("TOTAL = ", row[3], "\n")
print("Actualización realizada satisfactoriamente")
conn.close()
