from moviepy.editor import VideoFileClip
from PIL import Image, ImageDraw, ImageFont
import os

def extract_frame(video_path, frame_time, output_path):
    video = VideoFileClip(video_path)
    frame = video.get_frame(frame_time)
    video.close()
    
    frame_image = Image.fromarray(frame)
    frame_image.save(output_path)

def write_text_with_filename(image_path):
    # Open the image
    image = Image.open(image_path)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Define the text and font properties
    text = os.path.basename(image_path)
    font_size = 24
    font = ImageFont.truetype("arial.ttf", font_size)
    text_color = (255, 255, 255)  # White color

    # Determine the position to place the text
    text_width, text_height = draw.textsize(text, font=font)
    x = image.width - text_width - 10
    y = image.height - text_height - 10

    # Write the text on the image
    draw.text((x, y), text, font=font, fill=text_color)

    # Save the modified image
    output_path = f"output_{os.path.basename(image_path)}"
    image.save(output_path)

    print(f"Text added to the image: {output_path}")

for archivo in os.listdir("../../../001-Blender_3/video"):
    video_path = "../../../001-Blender_3/video/"+archivo
    try:
        os.mkdir("imagenes")
    except:
        pass
    output_path = 'imagenes/'+archivo+'.jpg'
    try:
        extract_frame(video_path, 10, output_path)
    except:
        print("error en la imagen")

for archivo in os.listdir("imagenes"):
    write_text_with_filename("imagenes/"+archivo)











    
