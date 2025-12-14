from ultralytics import YOLO
import glob
import os

model = YOLO("yolov8n.pt")
input_folder = "frames"
output_folder = "processed_frames"
os.makedirs(output_folder, exist_ok=True)

for img_path in glob.glob(f"{input_folder}/*.jpg"):
    results = model(img_path)
    results[0].save(output_folder)


