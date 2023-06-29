from moviepy.editor import ImageSequenceClip
import os
from PIL import Image,ImageDraw,ImageFont
import random

def frames_to_video(frames_folder, output_path, fps):
    frames = sorted(os.listdir(frames_folder))
    frame_paths = [os.path.join(frames_folder, frame) for frame in frames]
    clip = ImageSequenceClip(frame_paths, fps=fps)
    output_name, output_ext = os.path.splitext(output_path)
    codec = 'libx264'
    clip.write_videofile(output_path, codec=codec)
    print(f"Video created: {output_path}")

width = 1920
height = 1080
background_color = (0,0,0,255)
font_path = "matrix.ttf"
font_size = 48
lista = []
for i in range(0,int(width/font_size)*int(height/font_size)):
    numero = random.randint(0,255)
    if numero < 20:
        anade = 255
    else:
        anade = 0
    lista.append(anade)

letras = "abcdefghijklmnopqrstuvwxyz0123456789"


font = ImageFont.truetype(font_path, font_size)
for i in range(0,50):
    nuevalista = []
    for j in range(0,int(width/font_size)*int(height/font_size)):
        nuevalista.append(255)
    for j in range(int(width/font_size),len(lista)-int(width/font_size)-1):
        #print(i-width)
        nuevalista[j] = lista[j-round(width/font_size)]
    print(nuevalista)
    contador = 0
    imagen = Image.new("RGBA", (width, height), background_color)
    draw = ImageDraw.Draw(imagen)
    for x in range(width,0,-font_size):
        for y in range(height,0,-font_size):
            
            text = letras[random.randint(0,len(letras)-1)]
            text_position = (x, y)
            try:
                if lista[contador] == 255:
                    text_color = (34, 180, 85, lista[contador])
                else:
                    #print(int(lista[contador-width]*0.9))
                    text_color = (34, 180, 85, int(lista[contador-int(width/font_size)]*0.9))
                draw.text(text_position, text, font=font, fill=text_color)
            except:
                pass
            contador += 1
            
    #imagen.show()
    imagen.save("imagenes/"+str(i)+".png")
    for j in range(0,len(nuevalista)):
        
        lista[j] = nuevalista[j]

##print("vamos al video")
##frames_folder = 'imagenes'
##output_path = 'matrix.mp4'
##fps = 24
##frames_to_video(frames_folder, output_path, fps)




