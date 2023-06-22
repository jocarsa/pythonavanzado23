import tkinter as tk
import subprocess

raiz = tk.Tk()
raiz.geometry("500x500")

proc = subprocess.Popen(['python', 'p011-LlamadaTablas.py',  ''], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
resultado = proc.communicate()[0].decode('utf8')
print(type(resultado))
listatablas = list(resultado)
print(listatablas)

raiz.mainloop()
