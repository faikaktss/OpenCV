#Görüntülere uygulayabileceğimiz birçok farklı efekt ve 
# filtre var. Burada sadece birkaçını gözden geçireceğiz.
#  Çoğu, tüm piksel değerlerine uygulanan bir tür matematik tabanlı 
# işlev içerir.

import warnings
warnings.filterwarnings("ignore")

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def load_img():
    img = cv2.imread('../Ekran Resmi 2025-12-03 20.22.51.png').astype(np.float32)  / 255.0
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    return img

def display_img(img):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    ax.imshow(img)

i = load_img()
display_img(i)


#Gama Düzeltemsi
#Saydamlaştır
img = load_img()
gamma = 1/4
effected_img = np.power(img,gamma)
display_img(effected_img)

#Netleştirme
img = load_img()
gamma = 2
effected_img = np.power(img,gamma)
display_img(effected_img)

#2D Konvolüsyonlu DÜşük Geçiş Filtresi

img = load_img()
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img=img,text='OpenCV',org=(50,150),fontFace=font,fontScale=3,color=(255,0,0),thickness=5)
display_img(img)



#Gürültü Ekleme
img = cv2.imread('../Ekran Resmi 2025-12-03 20.22.51.png').astype(np.float32)  / 255.0
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

display_img(img)

