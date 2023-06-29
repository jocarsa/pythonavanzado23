from PIL import Image,ImageDraw,ImageFont
import random

width = 1920
height = 1080
background_color = (0,0,0,255)  
imagen = Image.new("RGBA", (width, height), background_color)

# Create a drawing object
draw = ImageDraw.Draw(imagen)

letras = "abcdefghijklmnopqrstuvwxyz0123456789"

font_path = "matrix.ttf"
font_size = 24
font = ImageFont.truetype(font_path, font_size)
for x in range(0,width,font_size):
    for y in range(0,height,font_size):
        text = letras[random.randint(0,len(letras)-1)]
        text_position = (x, y)
        text_color = (34, 180, 85, random.randint(0,255))  # RGB value for black
        draw.text(text_position, text, font=font, fill=text_color)
        




imagen.show()
#imagen.save("rectangle_image.jpg")
