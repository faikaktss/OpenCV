import cv2
import numpy as np
import matplotlib.pyplot as plt 

flat_chess = cv2.imread("../Ders Notları/images/flat_chessboard.png")
flat_chess = cv2.cvtColor(flat_chess, cv2.COLOR_BGR2GRAY)
plt.imshow(flat_chess,cmap='gray')
plt.title("Düz Satranç Tahtası")
plt.show()

gray_flat_chess = cv2.cvtColor(flat_chess, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_flat_chess,cmap='gray')
plt.title("Gri Tonlamalı Düz Satranç Tahtası")
plt.show()


real_chess = cv2.imread("../Ders Notları/images/real_chessboard.png")   
real_chess = cv2.cvtColor(real_chess, cv2.COLOR_BGR2GRAY)
plt.imshow(real_chess,cmap='gray')
plt.title("Gerçek Satranç Tahtası")
plt.show()

gray_real_chess = cv2.cvtColor(real_chess, cv2.COLOR_BGR2GRAY)
plt.imshow(gray_real_chess,cmap='gray')
plt.title("Gri Tonlamalı Gerçek Satranç Tahtası")
plt.show()


# Köşe Tespiti - Harris Yöntemi

gray = np.float32(gray_flat_chess)

dst = cv2.cornerHarris(src=gray,blockSize=2,ksize=3,k=0.04)
dst = cv2.dilate(dst,None)

flat_chess[dst>0.01*dst.max()] = [0,0,255]
plt.imshow(flat_chess,cmap='gray')
plt.title("Köşe Tespiti - Düz Satranç Tahtası")
plt.show()

gray = np.float32(gray_real_chess)

dst = cv2.cornerHarris(src=gray,blockSize=2,ksize=3,k=0.04)
dst = cv2.dilate(dst,None)#Köşe noktalarını belirginleştirme

real_chess[dst>0.01*dst.max()] = [0,0,255]
plt.imshow(real_chess,cmap='gray')
plt.title("Köşe Tespiti - Gerçek Satranç Tahtası")
plt.show()



#Shi-Tomasi Köşe Dedektörü ve Kağıdı İzlemek İçin İyi Özellikler

flat_chess = cv2.imread("../Ders Notları/images/flat_chessboard.png")
flat_chess = cv2.cvtColor(flat_chess, cv2.COLOR_BGR2GRAY)
gray_flat_chess = cv2.cvtColor(flat_chess, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,5,0.01,10) #float döndürür ondan dolayı int yaptık
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(flat_chess,(x,y),3,255,-1)

plt.imshow(flat_chess,cmap='gray')