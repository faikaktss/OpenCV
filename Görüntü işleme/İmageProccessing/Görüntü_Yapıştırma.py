# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from PIL import Image
# import os

# img1 = cv2.imread('../Ekran Resmi 2025-12-03 20.22.51.png')
# img2 = cv2.imread('../Ekran Resmi 2025-12-03 20.22.51.png')

# print(img1.shape)
# print(img2.shape)

# plt.imshow(img1)

# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# plt.imshow(img1)
# plt.imshow(img2)

# img1 = cv2.resize(img1,(600,400))
# img2 = cv2.resize(img2,(600,400))


# plt.imshow(img1)
# plt.imshow(img2)


# #Görüntü yapıştırma işlemi
# blended = cv2.addWeighted(src1=img1,alpha=0.7,src2=img2,beta=0.3,gamma=0)
# plt.imshow(blended)


# #Farklı boyutlarda görüntüleri üst üste bindirmek
# img1 = cv2.imread('../Ekran Resmi 2025-12-03 20.22.51.png')
# img2 = cv2.imread('../Ekran Resmi 2025-12-03 20.22.51.png')
# img2 = cv2.resize(img2,(600,600))

# img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
# img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# large_img = img1
# small_img = img2


# #Küçük görüntüyü büyük görüntünün üzerine yapıştırma koordinatları
# x_offset = 0
# y_offset = 0

# large_img[y_offset:y_offset+small_img.shape[0], x_offset:x_offset+small_img.shape[1]] = small_img
# plt.imshow(large_img)


#Farklı boyutlardaki görüntüleri karıştırmak


import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('../Ekran Resmi 2025-12-03 20.22.51.png')
img2 = cv2.imread('../Ekran Resmi 2025-12-03 20.22.51.png')
img2 = cv2.resize(img2,(600,600))

img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB )
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.imshow(img1)
plt.imshow(img2)

print(img1.shape)


xoffset = 934-600
yoffset = 1401-600

rows ,cols,channels = img2.shape
roi = img1[yoffset:1401,xoffset:934]

plt.imshow(roi)


#Maske oluşturma

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
print(img2gray.shape)

plt.imshow(img2gray,cmap='gray')

mask_inv =cv2.bitwise_not(img2gray)#Her pikselin değerini tersine çevirir

print(mask_inv.shape)

plt.imshow(mask_inv,cmap='gray')

