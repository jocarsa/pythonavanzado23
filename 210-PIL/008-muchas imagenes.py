import math
from PIL import Image, ImageDraw
import random
import os

try:
    os.mkdir("imagenes")
except:
    print("la carpeta ya existe")

anchura = 2048
altura = 2048

imagen = Image.new("RGBA", (anchura, altura))

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

contador = 1
for j in range(0,100):
    dibujo = ImageDraw.Draw(imagen)
    for i in range(0,50000):
        x=  random.randint(0,anchura)
        y = random.randint(0,altura)
        rojo = random.randint(0,255)
        verde = random.randint(0,255)
        azul = random.randint(0,255)
        rojo2 = random.randint(0,255)
        verde2 = random.randint(0,255)
        azul2 = random.randint(0,255)
        dibujo.rectangle(
            [
                (
                    x,
                    y
                ),
                (
                    x+random.randint(0,50),
                    y+random.randint(0,50)
                )
            ],
            fill =rgb_to_hex(rojo, verde, azul),
            outline =rgb_to_hex(rojo2, verde2, azul2)
            )
    imagen.save("imagenes/imagen"+str(j)+".png")











