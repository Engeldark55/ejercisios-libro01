import sqlite3 as db

def conecte():
    conn = db.connect('db_main.db')
    return conn

def insert_prod(data):
    conexion = conecte()
    conexion.execute(" INSERT INTO Producto(clave, nombre, cantidad, tipo, pre_compra, pre_venta, descripcion, fecha) VALUES(?,?,?,?,?,?,?,?)", data)
    conexion.commit()
    conexion.close()
    