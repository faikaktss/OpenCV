import numpy as np
import matplotlib.pyplot as plt
import cv2
import os 

#Görüntüler üzerinde çizim işlemleri
blank_image = np.zeros((500,500,3),dtype=np.int16)
print(blank_image.shape)
cv2.imshow("Blank Image", blank_image)
cv2.waitKey()


#Şekil çizme işlemleri

cv2.rectangle(blank_image,pt1=(384,0),pt2=(510,128),color=(0,255,0),thickness=5)
plt.imshow(blank_image)

#Çember çizme işlemi
cv2.circle(img=blank_image,center=(250,250), radius=50, color=(255,0,0),thickness=5)
plt.imshow(blank_image)

#Çokgen çizme işlemi
blank_image = np.zeros((500,500,3),dtype=np.int16)
vertices = np.array([[100,300],[200,200],[400,300],[200,400]], np.int32)
pts = vertices.reshape((-1,1,2))
print(pts)

cv2.polylines(blank_image,[pts],isClosed=True,color=(0,255,255),thickness=3)
plt.imshow(blank_image)