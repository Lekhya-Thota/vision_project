from ultralytics import YOLO
import glob


model = YOLO('yolov8n.pt')


image_files = glob.glob('images/*.jpg')


for img_path in image_files:
    results = model(img_path)
    results[0].show()
    results[0].save('runs/detect/predict')

print("Detection completed for all images.")
