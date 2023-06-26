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

titulos = []
carpeta = 'seo/'
elementos = os.listdir(carpeta)
for elemento in elementos:
    titulos.append({"titulo":elemento,"logo":"html5.png"})

print(titulos)

carpeta = 'fondos/'
fondos = os.listdir(carpeta)
print(fondos)

for titulo in titulos:
    
    anchura = 1080
    altura = 1080

    imagen = Image.new("RGB", (anchura, altura))
    
    
    
    fondo = 'fondos/'+fondos[random.randint(0,len(fondos)-1)]
    imagenfondo = Image.open(fondo)
    imagen.paste(imagenfondo, (0,0))

    fondo = 'fondotrans/fondotrans.png'
    imagenfondo = Image.open(fondo).convert('RGBA')
    imagen.paste(imagenfondo, (0,0),mask=imagenfondo)

    fondo = 'fondotrans/fondotrans.png'
    imagenfondo = Image.open(fondo).convert('RGBA')
    imagen.paste(imagenfondo, (0,0),mask=imagenfondo)

    logo = 'logos/'+titulo["logo"]
    imagenlogo = Image.open(logo).convert('RGBA')
    imagenlogoreescalado = imagenlogo.resize((int(anchura/2), int(altura/2)))
    print(imagenlogoreescalado.size)
    imagen.paste(imagenlogoreescalado,
                 (  int(anchura/2-imagenlogoreescalado.size[0]/2)
                     ,int(altura/2-imagenlogoreescalado.size[1]/2+altura/8)
                    ),
                 mask=imagenlogoreescalado)
    
    width = 1080
    height = 1080
    draw = ImageDraw.Draw(imagen)
    texto = titulo["titulo"]
    font_size = 64
    font_color = (0, 0, 0)  
    font_path = "fuentes/Ubuntu-Bold.ttf"  
    font = ImageFont.truetype(font_path, font_size)
    text_width, text_height = draw.textsize(texto, font=font)
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2-height/4
    draw.text((text_x, text_y), texto, font=font, fill=font_color)

    #imagen.show()
    imagen.save("resultado/"+titulo["titulo"]+".png")












