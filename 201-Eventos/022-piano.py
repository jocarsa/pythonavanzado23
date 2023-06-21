import tkinter as tk
import threading
from playsound import playsound
import time

anchura = 1400
altura = 300
numteclas = 50
anchotecla = 30
reproducciones = []
nota = {}
teclas = {}
notas = ['C','D','E','F','G','A','B']
escala = [0,1,2,3,4,5,6,7]
for nombrenota in notas:
    for numeroescala in escala:
        nota[nombrenota+str(numeroescala)] = "mp3/"+nombrenota+str(numeroescala)+".mp3"
print(nota)

def dibujaPiano():
    i = 0
    for numeroescala in escala:
        for nombrenota in notas:
            teclas[nombrenota+str(numeroescala)] = lienzo.create_rectangle(
                i*anchotecla+20,
                20,
                i*anchotecla+anchotecla+20,
                altura-20,
                fill="white"
                )
            i+=1
    print(teclas)

    alteraciones = [0,1,3,4,5]

    for i in range(0,7):
        for alteracion in alteraciones:
            lienzo.create_rectangle(
                    i*anchotecla*7+alteracion*anchotecla+20+anchotecla/2+anchotecla/4,
                    20,
                    i*anchotecla*7+alteracion*anchotecla+20+anchotecla/2+anchotecla-anchotecla/4,
                    altura-120,
                    fill="black"
                    )
def pulsaTecla(dimelanota):
    reproducciones.append(
        threading.Thread(target=playsound,
                         args=(nota[dimelanota],),
                         daemon=True).start()
        )
    

def dimeAlgo():
    print("te digo algo")
def keydown(event):
    print("has pulsado una tecla:"+event.char)
    if(event.char == "a"):
        pulsaTecla("C4")
        lienzo.itemconfig(teclas["C4"], fill='green')
    elif(event.char == "s"):
        pulsaTecla("D4")
        lienzo.itemconfig(teclas["D4"], fill='green')
    elif(event.char == "d"):
        pulsaTecla("E4")
        lienzo.itemconfig(teclas["E4"], fill='green')
    elif(event.char == "f"):
        pulsaTecla("F4")
        lienzo.itemconfig(teclas["F4"], fill='green')
    elif(event.char == "g"):
        pulsaTecla("G4")
        lienzo.itemconfig(teclas["G4"], fill='green')
    elif(event.char == "h"):
        pulsaTecla("A4")
        lienzo.itemconfig(teclas["A4"], fill='green')
    elif(event.char == "j"):
        pulsaTecla("B4")
        lienzo.itemconfig(teclas["B4"], fill='green')
    elif(event.char == "k"):
        pulsaTecla("C5")
        lienzo.itemconfig(teclas["C5"], fill='green')
    elif(event.char == "l"):
        pulsaTecla("D5")
        lienzo.itemconfig(teclas["D5"], fill='green')
def keyup(event):
    print("has despulsado una tecla:"+event.char)
    if(event.char == "a"):
        lienzo.itemconfig(teclas["C4"], fill='white')
    elif(event.char == "s"):
        lienzo.itemconfig(teclas["D4"], fill='white')
    elif(event.char == "d"):
        lienzo.itemconfig(teclas["E4"], fill='white')
    elif(event.char == "f"):
        lienzo.itemconfig(teclas["F4"], fill='white')
    elif(event.char == "g"):
        lienzo.itemconfig(teclas["G4"], fill='white')
    elif(event.char == "h"):
        lienzo.itemconfig(teclas["A4"], fill='white')
    elif(event.char == "j"):
        lienzo.itemconfig(teclas["B4"], fill='white')
    elif(event.char == "k"):
        lienzo.itemconfig(teclas["C5"], fill='white')
    elif(event.char == "l"):
        lienzo.itemconfig(teclas["D5"], fill='white')
raiz = tk.Tk()
raiz.geometry(str(anchura)+"x"+str(altura))

marco = tk.Frame(raiz,width=anchura,height=altura)
marco.pack()

lienzo = tk.Canvas(marco,width=anchura,height=altura)
lienzo.pack()

dibujaPiano()


raiz.bind("<KeyPress>", keydown)
raiz.bind("<KeyRelease>", keyup)

    

raiz.mainloop()









