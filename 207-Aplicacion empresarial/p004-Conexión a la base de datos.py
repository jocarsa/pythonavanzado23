#pip install mysql-connector-python
import mysql.connector

conexion = mysql.connector.connect(
    user='aplicacion',
    password='aplicacion',
    host='localhost',
    database='aplicacion')

conexion.close()
