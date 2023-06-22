#pip install mysql-connector-python
import mysql.connector
import json
import sys
import ast

with open('configuracion.json') as archivo:
    datos = json.load(archivo)
    conexion = mysql.connector.connect(
        user=datos['usuario'],
        password=datos['contrasena'],
        host=datos['servidor'],
        database=datos['basededatos']
        )
    cursor = conexion.cursor()
    
def insertaRegistro(tabla,datos):  
    peticion = "INSERT INTO "+tabla+" VALUES (NULL,"
    datolista = ast.literal_eval(datos)
    print(datolista)
    datolista = datolista[1:]
    for dato in datolista:
        print("el dato es: "+dato)
        peticion += "'"+dato+"',"
    peticion = peticion[:-1]
    peticion += ")"
    print(peticion)
    cursor.execute(peticion)
    print("en la tabla "+tabla+" voy a insertar los datos "+datos)
    conexion.commit()

insertaRegistro(str(sys.argv[1:][0]),str(sys.argv[2:][0]))
  
conexion.close()
