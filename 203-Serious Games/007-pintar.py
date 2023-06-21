import tkinter as tk
from tkinter import *




class Personaje:
    def __init__(self):
        self.px = 20
        self.py = 20

def pulsaTecla(event):
    global px
    global py
    global personaje
    print("has pulsado una tecla "+event.char)
    if event.char == "w":
        print("arriba")
        lienzo.itemconfig(personaje, fill='white')
        lienzo.move(personaje, 0, -10)
    elif event.char == "s":
        print("abajo")
        lienzo.move(personaje, 0, +10)
    elif event.char == "a":
        print("izquierda")
        lienzo.move(personaje, -10, 0)
    elif event.char == "d":
        print("derecha")
        lienzo.move(personaje, 10, 0)
        
        

def despulsaTecla(event):
    print("has despulsado una tecla "+event.char)

raiz = tk.Tk()
raiz.geometry("512x512")

marco = tk.Frame(raiz,width=512,height=512)
marco.pack()

lienzo = tk.Canvas(marco,width=512,height=512)
lienzo.pack()
mariquita = PhotoImage(file='mariquita.png')
#personaje = lienzo.create_oval(10,10,20,20,fill="red")
personaje = lienzo.create_image(10,10,image=mariquita,anchor='nw') 



raiz.bind("<KeyPress>", pulsaTecla)
raiz.bind("<KeyRelease>", despulsaTecla)


raiz.mainloop()
