from moviepy.editor import VideoFileClip
from PIL import Image
import os

def extract_frame(video_path, frame_time, output_path):
    video = VideoFileClip(video_path)
    frame = video.get_frame(frame_time)
    video.close()
    
    frame_image = Image.fromarray(frame)
    frame_image.save(output_path)

for archivo in os.listdir("../../../001-Blender_3/video"):
    video_path = "../../../001-Blender_3/video/"+archivo
    try:
        os.mkdir("imagenes")
    except:
        pass
    output_path = 'imagenes/'+archivo+'.jpg'

    extract_frame(video_path, 10, output_path)
