import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

img = cv2.imread('../Ekran Resmi 2025-12-03 20.22.51.png')
plt.imshow(img)

img = cv2.imread('../Ekran Resmi 2025-12-03 20.22.51.png')
plt.imshow(img,cmap="gray")


#İkili Eşikleme
ret ,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
plt.imshow(thresh1,cmap="gray")

#İkili Ters Eşikleme
ret, thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
plt.imshow(thresh2,cmap="gray")

#Trunc Eşikleme
ret, thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
plt.imshow(thresh3,cmap="gray")

#Tozero Eşikleme
ret, thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
plt.imshow(thresh4,cmap="gray")


#Gerçek dünya uygulamaları
img = cv2.imread('../Ekran Resmi 2025-12-03 20.22.51.png',0)   

def show_pic(img):
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')

show_pic(img)

#Basit ikili
ret, th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
show_pic(th1)

#Gelişmiş hali
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
show_pic(th2)

th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
show_pic(th3)

blended = cv2.addWeighted(src1=th1,alpha=0.5,src2=th2,beta=0.5,gamma=0)
show_pic(blended)