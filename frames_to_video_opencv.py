import cv2
import glob

frame_paths = sorted(glob.glob("processed_frames/frame_*.jpg"))
if not frame_paths:
    print("No images found in processed_frames folder!")
    exit()

frame = cv2.imread(frame_paths[0])
height, width, layers = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('output_football.mp4', fourcc, 2, (width, height))  # 2 fps

for img_path in frame_paths:
    frame = cv2.imread(img_path)
    video.write(frame)

video.release()
print("Created video output_video.mp4")

