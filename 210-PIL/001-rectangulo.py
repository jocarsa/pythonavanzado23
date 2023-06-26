import math
from PIL import Image, ImageDraw

imagen = Image.new("RGB", (512, 512))
  
dibujo = ImageDraw.Draw(imagen)  
dibujo.rectangle([(20,20),(40,40)], fill ="#ff0000", outline ="#00ff00")
imagen.show()
