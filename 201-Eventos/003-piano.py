import tkinter as tk

raiz = tk.Tk()
raiz.geometry("800x300")

marco = tk.Frame(raiz,width=800,height=300)
marco.pack()

lienzo = tk.Canvas(marco,width=800,height=300)
lienzo.pack()

raiz.mainloop()
