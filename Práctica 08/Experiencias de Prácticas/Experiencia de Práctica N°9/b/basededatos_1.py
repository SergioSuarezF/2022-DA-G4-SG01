#basededatos_1.py
import sqlite3

conn = sqlite3.connect('pedidos.db')
print("Base de datos abierta satisfactoriamente")