from moviepy.editor import VideoFileClip
from PIL import Image


def duracion(video_path):
    video = VideoFileClip(video_path)
    duration = video.duration
    return duration

print("la duración del video es:"+str(duracion('video.mp4')))

findelvideo = duracion('video.mp4')
def extract_frame(video_path, frame_time, output_path):
    video = VideoFileClip(video_path)
    frame = video.get_frame(frame_time)
    video.close()
    
    frame_image = Image.fromarray(frame)
    frame_image.save(output_path)

video_path = 'video.mp4'
for i in range(0,int(findelvideo),10):
    frame_time = i

    output_path = 'frame'+str(i)+'.jpg'

    extract_frame(video_path, frame_time, output_path)
