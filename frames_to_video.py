from moviepy.editor import ImageSequenceClip
import glob

frame_paths = sorted(glob.glob("processed_frames/frame_*.jpg"))
clip = ImageSequenceClip(frame_paths, fps=2)  # Same fps as extraction
clip.write_videofile("output_football.mp4", codec="libx264")
