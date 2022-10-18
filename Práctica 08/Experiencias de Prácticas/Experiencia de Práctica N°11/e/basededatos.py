#Unir tablas
import sqlite3
conn = sqlite3.connect('pedidos.db')
print("Base de datos abierta satisfactoriamente")
cur = conn.cursor()
cur.execute(
    '' "SELECT * , users.fname, users.lname FROM orders LEFT JOIN users ON users.userid=orders.userid" "")
print(cur.fetchall())
print("Consulta realizada satisfactoriamente")
conn.close()