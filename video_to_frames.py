from moviepy.editor import VideoFileClip
import os

video_path = "football.mp4"
output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

clip = VideoFileClip(video_path)


for i, frame in enumerate(clip.iter_frames(fps=2)):
    from PIL import Image
    img = Image.fromarray(frame)
    img.save(f"{output_dir}/frame_{i:04d}.jpg")


