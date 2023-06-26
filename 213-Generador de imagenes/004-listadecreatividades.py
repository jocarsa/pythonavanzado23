import math
from PIL import Image, ImageDraw, ImageFont
import random
import os

try:
    os.mkdir("resultado")
except:
    print("la carpeta ya existe")

try:
    os.mkdir("imagenes")
except:
    print("la carpeta ya existe")

titulos = [
        'Títulos en HTML',
        'Tipos de CSS',
        'Imágenes en HTML',
        'Componentes en Angular'
    ]

carpeta = 'fondos/'
archivos = os.listdir(carpeta)
print(archivos)

for titulo in titulos:

    anchura = 1080
    altura = 1080

    imagen = Image.new("RGB", (anchura, altura))

    fondo = 'fondos/bloquescinco0042.jpg'
    imagenfondo = Image.open(fondo)

    imagen.paste(imagenfondo, (0,0))
    width = 1080
    height = 1080
    draw = ImageDraw.Draw(imagen)
    texto = titulo
    font_size = 64
    font_color = (0, 0, 0)  
    font_path = "fuentes/Ubuntu-Bold.ttf"  
    font = ImageFont.truetype(font_path, font_size)
    text_width, text_height = draw.textsize(texto, font=font)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2
    draw.text((text_x, text_y), texto, font=font, fill=font_color)

    #imagen.show()
    imagen.save("resultado/"+titulo+".png")












