from moviepy.editor import VideoFileClip

def get_video_size(video_path):
    video = VideoFileClip(video_path)
    width = video.size[0]
    height = video.size[1]
    video.close()
    return width, height

# Provide the path to your video file
video_path = 'video.mp4'

# Call the function to get the video size
width, height = get_video_size(video_path)

# Print the video size
print(f"Width: {width}px, Height: {height}px")
