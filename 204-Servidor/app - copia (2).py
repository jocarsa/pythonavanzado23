from flask import Flask
from flask import request
app = Flask(__name__)

usuarios = []

@app.route('/', methods=['GET', 'POST'])
def inicio():
    global usuarios
    usuario = request.form.get('usuario')
    print(usuario)
    usuarios.append(usuario)
    return "Hola:"+usuarios

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)
