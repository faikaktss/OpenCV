import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

img = cv2.imread("../Ekran Resmi 2025-12-03 20.22.51.png")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)