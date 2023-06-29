from PIL import Image,ImageDraw

width = 1920
height = 1080
background_color = (50,50,50)  
imagen = Image.new("RGB", (width, height), background_color)

# Create a drawing object
draw = ImageDraw.Draw(imagen)

# Define the rectangle properties
rectangle_position = (50, 50, 200, 150)  # (x1, y1, x2, y2)
rectangle_outline_color = (255, 0, 0)  # RGB value for red
rectangle_outline_width = 2

# Draw the rectangle on the image
draw.rectangle(rectangle_position, outline=rectangle_outline_color, width=rectangle_outline_width)

imagen.save("rectangle_image.jpg")
