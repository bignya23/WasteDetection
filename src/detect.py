import cv2
import numpy as np
import torch

model = torch.hub.load('ultralytics/yolov5', 'custom', path='../runs/last.pt')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    mirrored_frame = cv2.flip(frame, 1)
    results = model(mirrored_frame)

    cv2.imshow('YOLO', np.squeeze(results.render()))

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()