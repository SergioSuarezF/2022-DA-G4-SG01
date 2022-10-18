#Prevencion de ataques
import sqlite3

conn = sqlite3.connect('pedidos.db')
cur = conn.cursor()
order = (5, '15/06/2015', 3, 400215)
cur.execute("INSERT INTO orders VALUES(?, ?, ?, ?);", order)
conn.commit()

moreOrders = [(6, '03/10/2021', 3, 2015478), (7, '02/01/2019', 3, 2015698)]
cur.executemany("INSERT INTO orders VALUES(?, ?, ?, ?);", moreOrders)
conn.commit()
