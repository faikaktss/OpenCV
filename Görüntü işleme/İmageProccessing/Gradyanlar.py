import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

img = cv2.imread('../Ekran Resmi 2025-12-03 20.22.51.png').astype(np.float32)  / 255.0

def display_img(img):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    ax.imshow(img ,cmap='gray')

display_img(img)
