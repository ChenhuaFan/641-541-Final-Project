import mediapipe as mp
import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import procrustes
from matplotlib.image import imread
import os

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

## Test the accuracy on the test set using procrustes.

# Run MediaPipe Hands and plot 3d hands world landmarks.
hands =  mp_hands.Hands(static_image_mode=True,max_num_hands=1, min_detection_confidence=0.5)

def get_landmark(file_path):
    # image = cv2.imread('../archive/asl_alphabet_train/asl_alphabet_train/A/A10.jpg')
    image = cv2.imread(file_path)

    # Convert the BGR image to RGB and process it with MediaPipe Hands.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    if not results.multi_hand_world_landmarks:
        return None

    a = results.multi_hand_world_landmarks[0].landmark
    landmarks = np.zeros(shape=(len(a), 3))
    for idx, item in enumerate(a):
        landmarks[idx, :] = np.array([item.x, item.y, item.z])

    return landmarks

classes = [chr(x) for x in range(ord('A'),ord('Z')+1)] + ['del', 'space']

lks = []
for i in classes:
    item_c = []
    for j in range(1,3000):
        path = f'../archive/asl_alphabet_train/asl_alphabet_train/{i}/{i}{j}.jpg'
        image = cv2.imread(path)
        # Convert the BGR image to RGB and process it with MediaPipe Hands.
        results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

        if not results.multi_hand_world_landmarks:
            continue

        a = results.multi_hand_world_landmarks[0].landmark
        landmarks = np.zeros(shape=(len(a), 3))
        for idx, item in enumerate(a):
            landmarks[idx, :] = np.array([item.x, item.y, item.z])
        item_c.append(landmarks)

        if(len(item_c)>20):
            break

    lks.append(np.mean(item_c, axis=0))

np.save('./shape.npy', lks)

list_d = []
for l in lks:
    list_d.extend(l)

dis = np.zeros(shape=(len(list_d),len(list_d)))

for i in range(0,len(list_d)):
    for j in range(i+1,len(list_d)):
        mtx1, mtx2, disparity = procrustes(list_d[i], list_d[j])
        dis[i][j] = disparity

dis = dis + dis.T
# make plot
fig, ax = plt.subplots()
# show image
shw = ax.imshow(dis)

# make bar
bar = plt.colorbar(shw)
plt.savefig('./shape_prove.eps', format='eps')
# show plot with labels
plt.show()
