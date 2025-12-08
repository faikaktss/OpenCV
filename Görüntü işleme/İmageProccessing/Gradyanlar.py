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



sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
laplacian = cv2.Laplacian(img,cv2.CV_64F)

display_img(sobelx)
display_img(sobely)
display_img(laplacian)


#Görüntüleri karıştırma
blended = cv2.addWeighted(src1=sobelx,alpha=0.5,src2=sobely,beta=0.5,gamma=0)
display_img(blended)
print(blended.shape)