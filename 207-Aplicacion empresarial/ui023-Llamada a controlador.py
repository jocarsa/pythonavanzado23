import tkinter as tk
import subprocess
import json
from tkinter import ttk

tablaactual = ""

def delete_all_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def muestraTabla(tabla):
    global tablaactual
    marcoinsertar.pack_forget()
    marco.pack()
    tablaactual = tabla
    print("te voy a mostrar la tabla: "+tabla)
    cargaDatos(tabla)

def cargaDatos(tabla):
    arbol.delete(*arbol.get_children())
    arbol.column("# 1", anchor=tk.CENTER)
    arbol.heading("# 1", text="1")
    arbol.column("# 2", anchor=tk.CENTER)
    arbol.heading("# 2", text="2")
    arbol.column("# 3", anchor=tk.CENTER)
    arbol.heading("# 3", text="3")

    # Cargar menu de tablas en TKInter
    proc = subprocess.Popen(['python', 'p012-Read.py',  tabla], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    resultado = proc.communicate()[0].decode('utf8')
    ojson = json.loads(resultado)
    print(type(ojson))
    for i in range(0,len(ojson)):
        print(ojson[i])
        arbol.insert('', 'end', text="1", values=(ojson[i][1], ojson[i][2], ojson[i][3]))
        pass
def nuevoRegistro():
    global tablaactual
    print("Insertamos un nuevo registro sobre la tabla: "+tablaactual)
    marco.pack_forget()
    marcoinsertar.pack()
    # Cargar menu de tablas en TKInter
    proc = subprocess.Popen(['python', 'p013-ListarColumnas.py',  tablaactual], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    resultado = proc.communicate()[0].decode('utf8')
    ojson = json.loads(resultado)
    print(type(ojson))
    marconuevoformulario
    delete_all_widgets(marconuevoformulario)
    
    for i in range(0,len(ojson)):
        print(ojson[i])
        listadovariables.append(tk.StringVar(raiz))
        tk.Label(marconuevoformulario,text="Insertar nuevo "+ojson[i][0]+":").pack()
        tk.Entry(marconuevoformulario,textvariable=listadovariables[-1]).pack()
    tk.Button(marconuevoformulario,text="Enviar",command=procesaEnviar).pack()
def procesaEnviar():
    listadovariablesstring = []
    for variable in listadovariables:
        print(variable.get())
        listadovariablesstring.append(variable.get())
    print("Voy a enviar el formulario")
    print(listadovariablesstring)
    proc = subprocess.Popen(['python', 'p014-InsertarRegistro.py',  tablaactual,json.dumps(listadovariablesstring)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    resultado = proc.communicate()[0].decode('utf8')
    print(resultado)
    
raiz = tk.Tk()
raiz.geometry("700x500")

listadovariables = []
listadovariablesstring = []
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
    menutablas.add_command(label=elemento[0],command=lambda elemento=elemento: muestraTabla(elemento[0]))

marco = tk.Frame(raiz,width=500,height=500)
marco.pack()
tk.Label(marco,text="Listado de tabla").pack()
tk.Button(marco,text="Crear nuevo registro",command=nuevoRegistro).pack()

arbol = ttk.Treeview(marco, column=("Nombre", "Telefono", "Email"), show='headings',height=10)

marcoinsertar= tk.Frame(raiz,width=500,height=500)
tk.Label(marcoinsertar,text="Insertamos un registro").pack()
marconuevoformulario = tk.Frame(marcoinsertar,width=500,height=500)
marconuevoformulario.pack()

arbol.pack()

raiz.mainloop()
