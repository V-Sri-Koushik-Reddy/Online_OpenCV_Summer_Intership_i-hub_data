from ultralytics import YOLO

model = YOLO("yolo26n.pt")
results = model("images.jpeg", save=True)

print("Detection completed.")
print("Results saved in runs/detect/predict")