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
    arbol.heading("# 1", text="Nombre")
    arbol.column("# 2", anchor=tk.CENTER)
    arbol.heading("# 2", text="Telefono")
    arbol.column("# 3", anchor=tk.CENTER)
    arbol.heading("# 3", text="Email")

    # Insert the data in Treeview widget
    arbol.insert('', 'end', text="1", values=('Juan', '1234', 'info@hola.com'))
    arbol.insert('', 'end', text="1", values=('Jorge', '1234', 'info@hola.com'))
    arbol.insert('', 'end', text="1", values=('Julia', '1234', 'info@hola.com'))
    arbol.insert('', 'end', text="1", values=('Jean', '1234', 'info@hola.com'))
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
    menutablas.add_command(label=elemento[0],command=lambda:muestraTabla("clientes"))

marco = tk.Frame(width=500,height=500)
marco.pack()
tk.Label(marco,text="Listado de tabla").pack()

arbol = ttk.Treeview(marco, column=("Nombre", "Telefono", "Email"), show='headings', height=5)


arbol.pack()

raiz.mainloop()
