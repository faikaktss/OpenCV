import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

def load_img():
    blank_img = np.zeros((600,600), dtype=np.uint8)
    font = cv2.FONT_HERSHEY_COMPLEX
    cv2.putText(blank_img,text='ABCDE',org=(50,300), fontFace=font,fontScale= 5,color=(255,255,255),thickness=25,lineType=cv2.LINE_AA)
    return blank_img

def display_img(img):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(111)
    ax.imshow(img,cmap='gray')

img = load_img()
display_img(img)


#Erozyon
#Ön plan nesnelerinin sınırlarını aşındırır
kernel = np.ones((5,5),np.uint8)
erosion1 = cv2.erode(img,kernel,iterations=1)

display_img(erosion1)

img = load_img()
kernel = np.ones((5,5),np.uint8)
erosion2 = cv2.erode(img,kernel,iterations=4)

display_img(erosion2)

#Açılış İşlemi
#Açılış erezyon ve ardından genişletme işlemi uygulamaktır.
#Buradaki görüntü cızırtılı bir görüntüdür.
img = load_img()
white_noise = np.random.randint(low=0,high=2,size=(600,600))
print(white_noise)

white_noise = white_noise * 255
print(white_noise.shape)

print(img.shape)

noise_img = white_noise + img
display_img(noise_img)



