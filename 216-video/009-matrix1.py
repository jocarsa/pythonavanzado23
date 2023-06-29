from PIL import Image,ImageDraw,ImageFont

width = 1920
height = 1080
background_color = (50,50,50)  
imagen = Image.new("RGB", (width, height), background_color)

# Create a drawing object
draw = ImageDraw.Draw(imagen)

# Define the text properties
text = "Hello, World!"
text_position = (50, 50)
text_color = (255,255,255)  # RGB value for black

# Load a TrueType font (replace with your own font file)
font_path = "matrix.ttf"
font_size = 24
font = ImageFont.truetype(font_path, font_size)

# Draw the text on the image
draw.text(text_position, text, font=font, fill=text_color)
imagen.show()
#imagen.save("rectangle_image.jpg")
