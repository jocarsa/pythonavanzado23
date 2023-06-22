from flask import Flask
from flask import request,render_template,Markup
import subprocess
import json

app = Flask(__name__)

# Cargar menu de tablas en TKInter
proc = subprocess.Popen(['python', 'p011-LlamadaTablas.py',  ''], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
resultado = proc.communicate()[0].decode('utf8')
ojson = json.loads(resultado)
print(ojson)
cadena = "<ul>"
for entrada in ojson:
    cadena += "<li><a href='?tabla="+entrada[0]+"'>"+entrada[0]+"</a></li>";
cadena += "</ul>"
    
@app.route('/', methods=['GET'])
def inicio():
    return render_template("index.html",menu=Markup(cadena), html_content=Markup(cadena))

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)
