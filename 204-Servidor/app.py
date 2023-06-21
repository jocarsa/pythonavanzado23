from flask import Flask
from flask import request

app = Flask(__name__)

usuarios = {}

@app.route('/', methods=['GET'])
def inicio():
    global usuarios
    usuario = request.args.get('usuario')
    px = request.args.get('px')
    py = request.args.get('py')
    usuarios[usuario] = {"px":px,"py":py}
    return usuarios

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
