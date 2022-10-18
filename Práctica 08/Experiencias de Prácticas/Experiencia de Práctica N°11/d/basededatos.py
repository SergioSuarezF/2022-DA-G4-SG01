#Fetchall
import sqlite3

conn = sqlite3.connect('pedidos.db')
print("Base de datos abierta satisfactoriamente")
cur = conn.cursor()
cur.execute("SELECT * FROM orders;")
all_results = cur.fetchall()
print(all_results)
print("Consulta realizada satisfactoriamente")
conn.close()
