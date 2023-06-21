import tkinter as tk

anchura = 1400
altura = 300

raiz = tk.Tk()
raiz.geometry(str(anchura)+"x"+str(altura))

marco = tk.Frame(raiz,width=anchura,height=altura)
marco.pack()

lienzo = tk.Canvas(marco,width=anchura,height=altura)
lienzo.pack()

numteclas = 50
anchotecla = 60

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

    

raiz.mainloop()









