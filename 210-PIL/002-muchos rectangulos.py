import math
from PIL import Image, ImageDraw
import random

imagen = Image.new("RGBA", (512, 512))
  
dibujo = ImageDraw.Draw(imagen)
for i in range(0,500):
    x=  random.randint(0,512)
    y = random.randint(0,512)
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
        ], fill ="#ff0000", outline ="#00ff00")
imagen.show()
