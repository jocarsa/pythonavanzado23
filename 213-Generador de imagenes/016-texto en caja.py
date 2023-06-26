import math
from PIL import Image, ImageDraw, ImageFont
import random
import os
import textwrap

            





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
    try:
        with open(carpeta+elemento, 'r') as file:
            file_text = file.read()
            reemplazado = elemento.split(".")[0].split("-")[1]
            print(reemplazado)
            titulos.append(
                {
                    "titulo":reemplazado,
                    "logo":"html5.png",
                    "contenido":file_text
                }
                )
    except:
        pass

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
    # Titulo de la imagen
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
    #Texto de párrafo de la imagen
    # Define the text content
    text = titulo["contenido"]

    # Define the font properties
    font_path = 'fuentes/Ubuntu-Regular.ttf'
    font_size = 24
    font_color = (0,0,0)  # RGB color tuple for white
    font = ImageFont.truetype(font_path, font_size)

    # Define the bounding box for the text
    box_width = 400
    box_height = 200
    box_position = (50, 50)  # Top-left position of the box

    # Draw a rectangle as the background for the text
    box_coords = (box_position[0], box_position[1],
                  box_position[0] + box_width, box_position[1] + box_height)
    ##draw.rectangle(box_coords, fill=(0, 0, 0))  # RGB color tuple for black

    # Calculate the position to place the text within the box
    text_x = box_position[0]
    text_y = box_position[1]

    # Wrap the text based on the box width
    wrapper = textwrap.TextWrapper(width=box_width // font_size)
    wrapped_text = wrapper.wrap(text)

    # Draw the wrapped text on the image within the bounding box
    for line in wrapped_text:
        line_width, line_height = draw.textsize(line, font=font)
        line_x = text_x + (box_width - line_width)
        draw.text((line_x, text_y), line, font=font, fill=font_color)
        text_y += font_size
        
    #imagen.show()
    imagen.save("resultado/"+titulo["titulo"]+".png")












