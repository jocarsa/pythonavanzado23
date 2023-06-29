from moviepy.editor import VideoFileClip
from PIL import Image

def extract_frame(video_path, frame_time, output_path):
    video = VideoFileClip(video_path)
    frame = video.get_frame(frame_time)
    video.close()
    
    frame_image = Image.fromarray(frame)
    frame_image.save(output_path)

# Provide the path to your video file
video_path = 'video.mp4'

# Provide the time (in seconds) of the frame you want to extract
frame_time = 10.0

# Provide the output path for the extracted frame image
output_path = 'frame.jpg'

# Call the function to extract the frame and save it as a JPEG image
extract_frame(video_path, frame_time, output_path)
