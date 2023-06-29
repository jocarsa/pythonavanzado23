from moviepy.editor import ImageSequenceClip
import os

def frames_to_video(frames_folder, output_path, fps):
    frames = sorted(os.listdir(frames_folder))
    frame_paths = [os.path.join(frames_folder, frame) for frame in frames]
    clip = ImageSequenceClip(frame_paths, fps=fps)
    output_name, output_ext = os.path.splitext(output_path)
    codec = 'libx264'
    clip.write_videofile(output_path, codec=codec)
    print(f"Video created: {output_path}")
frames_folder = 'imagenes'
output_path = 'output.mp4'
fps = 24
frames_to_video(frames_folder, output_path, fps)
