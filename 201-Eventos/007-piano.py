import tkinter as tk

anchura = 800
altura = 300

raiz = tk.Tk()
raiz.geometry(str(anchura)+"x"+str(altura))

marco = tk.Frame(raiz,width=anchura,height=altura)
marco.pack()

lienzo = tk.Canvas(marco,width=anchura,height=altura)
lienzo.pack()

numteclas = 20
anchotecla = 60

for i in range(0,numteclas):
    lienzo.create_rectangle(
        i*anchotecla+20,
        20,
        i*anchotecla+anchotecla+20,
        altura-20,
        fill="white"
        )

raiz.mainloop()
