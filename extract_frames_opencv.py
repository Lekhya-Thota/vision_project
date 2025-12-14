import cv2
import os

video_path = "video.mp4"
output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
frame_interval = int(fps / 2)

count = 0
i = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    if i % frame_interval == 0:
        cv2.imwrite(f"{output_dir}/frame_{count:04d}.jpg", frame)
        count += 1
    i += 1

cap.release()
print(f"Extracted {count} frames to {output_dir}/")
