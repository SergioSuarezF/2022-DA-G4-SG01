# Operacion Insertar
import sqlite3

conn = sqlite3.connect('pedidos.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS users(
 userid INT PRIMARY KEY,
 fname TEXT,
 lname TEXT,
 gender TEXT);
""")
conn.commit()
cur.execute("""CREATE TABLE IF NOT EXISTS orders(
 orderid INT PRIMARY KEY,
 date TEXT,
 userid TEXT,
 total TEXT);
""")
print("Base de datos abierta satisfactoriamente")
conn.execute("INSERT INTO ORDERS (ORDERID, DATE, USERID, TOTAL) \
 VALUES (1, '02/12/2021', 1, 20000)")
conn.execute("INSERT INTO ORDERS (ORDERID, DATE, USERID, TOTAL) \
 VALUES (2, '02/10/2021', 2, 210)")
conn.execute("INSERT INTO ORDERS (ORDERID, DATE, USERID, TOTAL) \
 VALUES (3, '04/12/2019', 3, 415203)")
conn.execute("INSERT INTO ORDERS (ORDERID, DATE, USERID, TOTAL) \
 VALUES (4, '02/09/2019', 4, 2541360)")
conn.commit()
print("Registros creados satisfactoriamente")
conn.close()
