import tkinter as tk

anchura = 800
altura = 400

raiz = tk.Tk()
raiz.geometry(str(anchura)+"x"+str(altura))

marco = tk.Frame(raiz,width=anchura,height=altura)
marco.pack()

lienzo = tk.Canvas(marco,width=anchura,height=altura)
lienzo.pack()

lienzo.create_rectangle(20,20,40,40,fill="white")

raiz.mainloop()
