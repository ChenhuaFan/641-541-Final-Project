import mediapipe as mp
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import procrustes
from matplotlib.image import imread
import os
from scipy.spatial import procrustes

from ASLDataset import ASLDataset

## Generate the average landmarks for each category.


mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles


# Run MediaPipe Hands and plot 3d hands world landmarks.
hands =  mp_hands.Hands(static_image_mode=True,max_num_hands=1, min_detection_confidence=0.3)

def get_landmark(image):
    # image = cv2.imread('../archive/asl_alphabet_train/asl_alphabet_train/A/A10.jpg')

    # Convert the BGR image to RGB and process it with MediaPipe Hands.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if not results.multi_hand_world_landmarks:
        return None

    a = results.multi_hand_world_landmarks[0].landmark
    landmarks = np.zeros(shape=(len(a), 3))
    for idx, item in enumerate(a):
        landmarks[idx, :] = np.array([item.x, item.y, item.z])

    return landmarks

lks = np.load('./shape.npy')
test_set = ASLDataset('test')


total = 0
correct = 0

for i in range(len(test_set)):

    image, label = test_set[i]


    pred = -1
    landmark = get_landmark(image)
    if landmark is None:
        pred = 28
        continue
    else:
        cal_dis = []
        for j in range(0, len(lks)):
            mtx1, mtx2, disparity = procrustes(lks[j], landmark)
            cal_dis.append(disparity)
        pred = np.argmin(cal_dis)

    if pred == label:
        correct += 1
    total += 1
    if i%500==0:
        print(f'Num: {i}, accuracy: {correct / total:.4f}')

print(correct / total)