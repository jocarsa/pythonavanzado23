from flask import Flask
from flask import request
from pymongo import MongoClient

app = Flask(__name__)

usuarios = {}

client = MongoClient("mongodb://localhost:27017");
mydb = client["juegopython"]
mycol = mydb["juego"]
print("Connection Successful")


@app.route('/', methods=['GET'])
def inicio():
    global usuarios
    usuario = request.args.get('usuario')
    px = request.args.get('px')
    py = request.args.get('py')
    usuarios[usuario] = {"px":px,"py":py}
    mycol.insert_one(usuarios)
    return usuarios

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
