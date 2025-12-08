import cv2
import numpy as np
import matplotlib.pyplot as plt


full = cv2.imread("../Ekran Resmi 2025-12-03 20.22.51.png")
full = cv2.cvtColor(full, cv2.COLOR_BGR2GRAY)

plt.imshow(full, cmap='gray')
plt.title("Orijinal Görüntü")
plt.show()


print(sum([1,2,3,4,5]))

my_string = "sum"
eval(my_string )# String içindeki yazıyı kod olarak çalıştırır


myFunc =eval(my_string)
myFunc([1,2,3,4,5])



height , width ,channels = full.shape
print(height , width ,channels)
