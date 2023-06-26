import math
from PIL import Image, ImageDraw
import random

imagen = Image.new("RGBA", (512, 512))

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)


dibujo = ImageDraw.Draw(imagen)
for i in range(0,5000):
    x=  random.randint(0,512)
    y = random.randint(0,512)
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
imagen.show()











