#Fetchone
import sqlite3

conn = sqlite3.connect('pedidos.db')
print("Base de datos abierta satisfactoriamente")
cur = conn.cursor()
cur.execute("SELECT * FROM orders;")
one_result = cur.fetchone()
print(one_result)
print("Consulta realizada satisfactoriamente")
conn.close()
