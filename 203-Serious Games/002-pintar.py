import tkinter as tk


def pulsaTecla(event):
    print("has pulsado una tecla "+event.char)
    if event.char == "w":
        print("arriba")
    elif event.char == "s":
        print("abajo")
    elif event.char == "a":
        print("izquierda")
    elif event.char == "d":
        print("derecha")
        

def despulsaTecla(event):
    print("has despulsado una tecla "+event.char)

raiz = tk.Tk()
raiz.geometry("512x512")

marco = tk.Frame(raiz,width=512,height=512)
marco.pack()

lienzo = tk.Canvas(marco,width=512,height=512)
lienzo.pack()

personaje = lienzo.create_oval(10,10,20,20,fill="red")



raiz.bind("<KeyPress>", pulsaTecla)
raiz.bind("<KeyRelease>", despulsaTecla)


raiz.mainloop()
