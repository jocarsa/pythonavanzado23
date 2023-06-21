import tkinter as tk

raiz = tk.Tk()
raiz.geometry("512x512")

marco = tk.Frame(raiz,width=512,height=512)
marco.pack()

lienzo = tk.Canvas(marco,width=512,height=512)
lienzo.pack()

lienzo.create_oval(10,10,20,20,fill="red")


raiz.mainloop()
