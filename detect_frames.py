from ultralytics import YOLO
import glob
import os
import cv2

model = YOLO("yolov8n.pt")
input_folder = "frames"
output_folder = "processed_frames"
os.makedirs(output_folder, exist_ok=True)

for img_path in glob.glob(f"{input_folder}/*.jpg"):
    results = model(img_path)

    annotated_img = results[0].plot()
    save_path = os.path.join(output_folder, os.path.basename(img_path))
    cv2.imwrite(save_path, annotated_img)

print(f"Saved processed images to {output_folder}/")
