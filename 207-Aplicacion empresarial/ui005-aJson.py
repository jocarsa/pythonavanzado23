import tkinter as tk
import subprocess
import json

raiz = tk.Tk()
raiz.geometry("500x500")

proc = subprocess.Popen(['python', 'p011-LlamadaTablas.py',  ''], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
resultado = proc.communicate()[0].decode('utf8')
print(type(resultado))
ojson = json.loads(resultado)
print(ojson)
for elemento in ojson:
    print(elemento[0])

raiz.mainloop()
