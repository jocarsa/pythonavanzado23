import math
from PIL import Image, ImageDraw
import random
import os

try:
    os.mkdir("imagenes")
except:
    print("la carpeta ya existe")

carpeta = 'fondos/'
archivos = os.listdir(carpeta)
print(archivos)



anchura = 1080
altura = 1080

imagen = Image.new("RGB", (anchura, altura))

imagen.show()












