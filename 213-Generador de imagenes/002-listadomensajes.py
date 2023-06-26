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

titulos = [
        'Primera creatividad',
        'Segunda creatividad',
        'Tercera creatividad'
    ]

anchura = 1080
altura = 1080

imagen = Image.new("RGB", (anchura, altura))

fondo = 'fondos/bloquescinco0042.jpg'
imagenfondo = Image.open(fondo)

imagen.paste(imagenfondo, (0,0))

imagen.show()












