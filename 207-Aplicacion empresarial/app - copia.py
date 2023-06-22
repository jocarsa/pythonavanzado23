from flask import Flask
from flask import request,render_template


app = Flask(__name__)


@app.route('/', methods=['GET'])
def inicio():
    return render_template("index.html",menu="hola")

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)
