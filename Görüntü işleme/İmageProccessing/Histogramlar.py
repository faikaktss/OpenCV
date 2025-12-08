import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

dark_horse = cv2.imread('../dark_horse.jpg').astype(np.float32)  / 255.0
show_horse = cv2.cvtColor(dark_horse,cv2.COLOR_BGR2RGB)

rainbow = cv2.imread('../rainbow.jpg').astype(np.float32)  / 255.0
show_rainbow = cv2.cvtColor(rainbow,cv2.COLOR_BGR2RGB)

blue_bricks = cv2.imread('../blue_bricks.jpg').astype(np.float32)  / 255.0
show_bricks = cv2.cvtColor(blue_bricks,cv2.COLOR_BGR2RGB)


#OpenCV Histogramı

# cv2.calcHist(görüntüler, kanallar, maske, histSize, aralıklar[, hist[, biriktirmek]])

# görüntüler: uint8 veya float32 türünün kaynak görüntüsüdür. köşeli parantez içinde, yani "[img]" olarak verilmelidir.
# kanallar: köşeli parantez içinde de verilir. Histogramı hesapladığımız kanal indeksidir. Örneğin, giriş gri tonlamalı görüntü ise, değeri [0]'dir. 
# Renkli görüntü için sırasıyla mavi, yeşil veya kırmızı kanalın histogramını hesaplamak için [0], [1] veya [2] iletebilirsiniz.
# maske : maske görüntüsü. Tam görüntünün histogramını bulmak için "Yok" olarak verilir. Ancak belirli bir görüntü bölgesinin histogramını bulmak istiyorsanız, 
# bunun için bir maske görüntüsü oluşturmanız ve maske olarak vermeniz gerekir. (Daha sonra bir örnek göstereceğim.)
# histSize: bu bizim BIN sayımızı temsil eder. Köşeli parantez içinde verilmesi gerekir. Tam ölçek için [256]'ı geçiyoruz.
# aralıklar: bu bizim ARALIĞIMız. Normalde [0,256]'dır.
