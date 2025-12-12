import cv2
import numpy as np
import matplotlib.pyplot as plt

road = cv2.imread("../Ders Notları/images/road.png")
road_copy = np.copy(road)
plt.imshow(road)


print(road.shape)


marker_image = np.zeros(road.shape[:2], dtype=np.int32)
segments = np.zeros(road.shape, dtype=np.uint8)
print(segments.shape)


from matplotlib import cm 

cm.tab10(0)
cm.tab10(1)

np.array(cm.tab10(0))
np.array(cm.tab10(0))[:3]
np.array(cm.tab10(0))[:3]*255

x = np.array(cm.tab10(0))[:3]*255

x = np.array(cm.tab10(0))[:3]*255

x.astype(int)

tuple(x.astype(int))


def create_rgb(i):
    x = np.array(cm.tab10(i))[:3]*255
    return tuple(x)

colors = []

for i in range(10):
    colors.append(create_rgb(i))
print(colors)