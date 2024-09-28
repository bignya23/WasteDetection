import torch
device = "Cuda" if torch.cuda.is_available() else "cpu"
print(device)
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')


# Run these Commands in terminal to train the model

#cd yolov5
# python train.py --img 320 --batch 16 --epochs 500 --data dataset.yml --weights yolov5s.pt --device 0





