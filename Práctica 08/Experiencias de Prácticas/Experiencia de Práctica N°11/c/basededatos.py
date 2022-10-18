#Fetchmany
import sqlite3

conn = sqlite3.connect('pedidos.db')
print("Base de datos abierta satisfactoriamente")
cur = conn.cursor()
cur.execute("SELECT * FROM orders;")
three_results = cur.fetchmany(3)
print(three_results)
print("Consulta realizada satisfactoriamente")
conn.close()
