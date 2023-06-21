from flask import Flask
from flask import request
app = Flask(__name__)

usuarios = []

@app.route('/', methods=['GET'])
def inicio():
    global usuarios
    usuario = request.form.get('usuario')
    print(request.form.get)
    print(usuario)
    usuarios.append(usuario)
    return usuarios

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
