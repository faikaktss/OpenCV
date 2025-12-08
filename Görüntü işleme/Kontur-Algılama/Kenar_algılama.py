import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../Ders Notları/images/sudoku.png")
plt.imshow(img,cmap='gray')
plt.title("Orijinal Görüntü")
plt.show()

edges = cv2.Canny(image=img,threshold1=100,threshold2=200)
plt.imshow(edges,cmap='gray')



#Görüntünün parlaklığına göre otomatik olarak kenar bulma
med_val = np.median(img)#Ortanca pikseli bulur

lower = int(max(0,0.7*med_val))
upper = int(min(255,1.3*med_val))

edges = cv2.Canny(image=img,threshold1=lower,threshold2=upper)
plt.imshow(edges,cmap='gray')
plt.title("Otomatik Kenar Algılama")
plt.show()

#Kenarları kalınlaştırma
blurred_img = cv2.blur(img,ksize=(5,5))
edges = cv2.Canny(image=blurred_img,threshold1=lower,threshold2=upper)
plt.imshow(edges,cmap='gray')
plt.title("Bulanıklaştırılmış Görüntü ile Kenar Algılama")
plt.show()