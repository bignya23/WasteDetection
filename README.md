# Garbage Classification using YOLOv5

This project focuses on object detection and classification of various types of waste using the YOLOv5 model. The model has been trained on a custom dataset to detect and classify different types of garbage, enabling efficient waste management and recycling.

## Dataset

The dataset used for training is from Kaggle: [Garbage Classification Dataset](https://www.kaggle.com/datasets/mostafaabla/garbage-classification). It contains various images of waste, categorized into multiple classes.

### Classes:
1. **E-Waste**
2. **Glass**
3. **Metal**
4. **Organic Waste**
5. **Paper/Cardboard**
6. **Plastic**
7. **Textiles**

### YOLOv5 Model:
- **Model**: `yolov5s` (small version of YOLOv5).
- **Training Epochs**: 21.
- **Image Size**: 320x320.
- **Batch Size**: 16.
- **Metrics (Epoch 21)**:
  - **Precision**: 0.88326
  - **Recall**: 0.87559
  - **mAP@0.5**: 0.93996
  - **mAP@0.5:0.95**: 0.8949
  - **Train Box Loss**: 0.0065196
  - **Train Objectness Loss**: 0.0050255
  - **Train Class Loss**: 0.015156

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/garbage-detection.git
cd garbage-detection

### 2. For live detection using a webcam
```bash

cd src
python detect.py
