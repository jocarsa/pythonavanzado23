import tkinter as tk
import subprocess
import json
from tkinter import ttk

def muestraTabla(tabla):
    print("te voy a mostrar la tabla: "+tabla)
    cargaDatos()

def cargaDatos():
    arbol.delete(*arbol.get_children())
    arbol.column("# 1", anchor=tk.CENTER)
    arbol.heading("# 1", text="1")
    arbol.column("# 2", anchor=tk.CENTER)
    arbol.heading("# 2", text="2")
    arbol.column("# 3", anchor=tk.CENTER)
    arbol.heading("# 3", text="3")

    # Cargar menu de tablas en TKInter
    proc = subprocess.Popen(['python', 'p012-Read.py',  ''], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    resultado = proc.communicate()[0].decode('utf8')
    ojson = json.loads(resultado)
    print(type(ojson))
    for i in range(0,len(ojson)):
        print(ojson[i])
        arbol.insert('', 'end', text="1", values=(ojson[i][1], ojson[i][2], ojson[i][3]))
        pass
        
raiz = tk.Tk()
raiz.geometry("700x500")

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
    menutablas.add_command(label=elemento[0],command=lambda:muestraTabla("clientes"))

marco = tk.Frame(width=500,height=500)
marco.pack()
tk.Label(marco,text="Listado de tabla").pack()

arbol = ttk.Treeview(marco, column=("Nombre", "Telefono", "Email"), show='headings',height=10)



arbol.pack()

raiz.mainloop()
