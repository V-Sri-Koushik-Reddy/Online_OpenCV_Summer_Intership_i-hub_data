# Conveyor nip-point hand intrusion detection

This repository contains my complete work during the Computer Vision Internship program under IIITH iHub-Data. The project focuses on building an end-to-end object detection pipeline using YOLO, including dataset creation, labeling, training, evaluation, and real-world inference.

# 📌 Project Objective

Idea: Detect when a worker’s hand, glove, or sleeve enters the dangerous pinch/nip zone of a moving conveyor or roller.

To build an AI-based object detection system capable of detecting:

- ✋ Human Hand  
- ⚠️ Danger Zone (Industrial Conveyor Safety Region)

# Key Highlights

- End-to-end computer vision pipeline  
- Video → frames → dataset → training → inference  
- Custom dataset creation using Label Studio  
- YOLO11n model training  
- Real-world conveyor video inference  
- Full ML workflow implementation  

# 📁 Repository Structure

```
Week-1/  → Video processing & frame extraction  
Week-2/  → OpenCV automation tasks  
Week-3/  → Dataset preparation  
Week-4/  → Labeling, training, evaluation  
Week-5/  → Final inference & testing  
```

# 🛠️ Tools & Technologies

- Python 3.x  
- OpenCV  
- Ultralytics YOLO (YOLO11n)  
- PyTorch  
- Label Studio  
- FFmpeg  
- Git & GitHub  
- macOS

# ⚙️ Model Details

- Model: YOLO11n  
- Image Size: 384x384  
- Epochs: 50  
- Optimizer: AdamW  
- Device: CPU (Apple M4)

# 📊 Performance Metrics

| Metric | Value |
|--------|------|
| Precision | 0.43 |
| Recall | 0.28 |
| mAP@50 | 0.31 |
| mAP@50-95 | 0.12 |

# 📌 Week-wise Work

# 🟦 Week 1
- Frame extraction using OpenCV  
- Video preprocessing  
- Dataset creation from videos  

# 🟩 Week 2
- Video automation pipelines  
- Frame processing improvements  
- Dataset structuring  

# 🟨 Week 3
- Dataset splitting (train/val/test)  
- YOLO format preparation  
- Label Studio setup  

# 🟥 Week 4
- Dataset annotation using Label Studio  
- YOLO11n training (50 epochs)  
- Model evaluation  
- Saved best.pt weights  

# 🟪 Week 5
- Inference on conveyor video  
- Bounding box predictions  
- Final output video generation    

# ⚙️ How to Run

## Clone repo
```bash
git clone https://github.com/your-username/repo.git
cd repo
```

## Install dependencies
```bash
pip install -r requirements.txt
```

## Run inference
```bash
yolo detect predict model=best.pt source=Week-5/video.mp4
```

# Important Files

- best.pt → final trained model  
- dataset.yaml → dataset config  
- week04_report.pdf → internship report  
- conveyor.mp4 → test video  

# Challenges

- Small dataset size  
- Label inconsistency early stage  
- Large GitHub file handling  

# Final Outcome

A working object detection system capable of detecting:

- Human hands  
- Conveyor danger zones  

# 🔮 Future Work

- Improve dataset size  
- Deploy real-time detection system  
- Upgrade to YOLOv8/v9  
- Optimize inference speed  

# 👨‍💻 Author

Sri Koushik Reddy  
IIITH iHub-Data Internship Project
