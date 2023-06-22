import tkinter as tk
import subprocess
import json

raiz = tk.Tk()
raiz.geometry("500x500")

mimenu = tk.Menu(raiz)
raiz.config(menu=mimenu)
menutablas = tk.Menu(mimenu)

mimenu.add_cascade(label="Archivo")
mimenu.add_cascade(label="Tablas",menu=menutablas)
mimenu.add_cascade(label="Ayuda")  

# Cargar menu de tablas en TKInter
proc = subprocess.Popen(['python', 'p011-LlamadaTablas.py',  ''], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
resultado = proc.communicate()[0].decode('utf8')
ojson = json.loads(resultado)
for elemento in ojson:
    menutablas.add_command(label=elemento[0])



raiz.mainloop()
