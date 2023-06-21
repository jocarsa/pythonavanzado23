import tkinter as tk
from tkinter import *
import json
import requests
import time
miusuario = ""
otrospersonajes = {}
otrospersonajesnombres = {}
class Personaje:
    def __init__(self):
        self.px = 20
        self.py = 20
px = 20
py = 20

def pulsaTecla(event):
    global px
    global py
    global personaje
    print("has pulsado una tecla "+event.char)
    if event.char == "w":
        print("arriba")
        py-=10
        lienzo.moveto(personaje, px, py)
  
    elif event.char == "s":
        print("abajo")
        py+=10
        lienzo.moveto(personaje, px, py)
    elif event.char == "a":
        print("izquierda")
        px-=10
        lienzo.moveto(personaje, px, py)
    elif event.char == "d":
        print("derecha")
        px+=10
        lienzo.moveto(personaje, px, py)

    bucle()
        
        

def despulsaTecla(event):
    print("has despulsado una tecla "+event.char)


def bucle():
    global miusuario
    global px
    global py
    cadena = "http://192.168.1.74/?usuario="+miusuario+"&px="+str(px)+"&py="+str(py)+""
    print(cadena)
    urlstring = cadena
    try:
        respuesta = requests.get(urlstring)
        respuesta.raise_for_status()
    except HTTPError as mierror:
        print(mierror)
    except Exception as errorpython:
        print(errorpython)
    else:
        respuesta.encoding ='utf-8'
        print(respuesta.text)
        cadenajson = json.loads(respuesta.text)
        print(cadenajson)
        for usuario in cadenajson:
            print(usuario)
            
            print(cadenajson[usuario])
            print(cadenajson[usuario]['px'])
            print(cadenajson[usuario]['py'])
            if usuario in otrospersonajes:
                lienzo.moveto(
                    otrospersonajes[usuario],
                    cadenajson[usuario]['px'],
                    cadenajson[usuario]['py']
                    )
                lienzo.moveto(
                    otrospersonajesnombres[usuario],
                    cadenajson[usuario]['px'],
                    int(cadenajson[usuario]['py'])-10
                    )
            else:
                otrospersonajes[usuario] = lienzo.create_image(
                    cadenajson[usuario]['px'],
                    cadenajson[usuario]['py'],
                    image=mariquita,
                    anchor='nw')
                otrospersonajesnombres[usuario] = lienzo.create_text(
                    cadenajson[usuario]['px'],
                    int(cadenajson[usuario]['py'])-10,
                    text=usuario
                    )
    
def asignaUsuario():
    global miusuario
    print("tu usuario es: "+nombremiusuario.get())
    miusuario = nombremiusuario.get()
    
raiz = tk.Tk()
raiz.geometry("512x512")
nombremiusuario = tk.StringVar()
marco = tk.Frame(raiz,width=512,height=512)
marco.pack()
tk.Label(marco,text="Introduce tu usuario").pack()
tk.Entry(marco,textvariable=nombremiusuario).pack()
tk.Button(marco,text="Envia",command=asignaUsuario).pack()
lienzo = tk.Canvas(marco,width=512,height=512)
lienzo.pack()
mariquita = PhotoImage(file='mariquita.png')
#personaje = lienzo.create_oval(10,10,20,20,fill="red")
personaje = lienzo.create_image(10,10,image=mariquita,anchor='nw') 

raiz.bind("<KeyPress>", pulsaTecla)
raiz.bind("<KeyRelease>", despulsaTecla)



bucle()





raiz.mainloop()
