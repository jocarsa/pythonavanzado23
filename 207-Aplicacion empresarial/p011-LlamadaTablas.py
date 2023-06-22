#pip install mysql-connector-python
import mysql.connector
import json
import sys

with open('configuracion.json') as archivo:
    datos = json.load(archivo)
    conexion = mysql.connector.connect(
        user=datos['usuario'],
        password=datos['contrasena'],
        host=datos['servidor'],
        database=datos['basededatos']
        )
    cursor = conexion.cursor()
    
def dameTablas():  
    peticion = "SHOW TABLES in "+datos['basededatos']
    cursor.execute(peticion)
    datosdb = cursor.fetchall()
    print(json.dumps( datosdb ))


dameTablas()
  
conexion.close()
