import tkinter as tk
import threading
from playsound import playsound

anchura = 1400
altura = 300
numteclas = 50
anchotecla = 60
reproducciones = []
nota = {}
notas = ['C','D','E','F','G','A','B']
escala = [0,1,2,3,4,5,6,7]
for nombrenota in notas:
    for numeroescala in escala:
        nota[nombrenota+str(numeroescala)] = "mp3/"+nombrenota+str(numeroescala)+".mp3"
print(nota)

def dibujaPiano():
    for i in range(0,numteclas):
        lienzo.create_rectangle(
            i*anchotecla+20,
            20,
            i*anchotecla+anchotecla+20,
            altura-20,
            fill="white"
            )

    alteraciones = [0,1,3,4,5]

    for i in range(0,5):
        for alteracion in alteraciones:
            lienzo.create_rectangle(
                    i*anchotecla*7+alteracion*anchotecla+20+anchotecla/2+anchotecla/4,
                    20,
                    i*anchotecla*7+alteracion*anchotecla+20+anchotecla/2+anchotecla-anchotecla/4,
                    altura-120,
                    fill="black"
                    )
def pulsaTecla():
    print("Has pulsado la tecla A")
    reproducciones.append(
        threading.Thread(target=playsound,
                         args=("mp3/C4.mp3",),
                         daemon=True).start()
        )

raiz = tk.Tk()
raiz.geometry(str(anchura)+"x"+str(altura))

marco = tk.Frame(raiz,width=anchura,height=altura)
marco.pack()

lienzo = tk.Canvas(marco,width=anchura,height=altura)
lienzo.pack()

dibujaPiano()

raiz.bind("<a>", lambda x: pulsaTecla())

    

raiz.mainloop()









