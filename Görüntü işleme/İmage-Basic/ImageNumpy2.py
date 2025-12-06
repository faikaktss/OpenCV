import numpy as np
import cv2
import matplotlib.pyplot as plt
import os


# img = cv2.imread(os.path.join(os.path.dirname(os.path.abspath(__file__)),"./Ekran Resmi 2025-12-03 20.22.51.png"))

# img_bgr = cv2.imread(os.path.join(os.path.dirname(os.path.abspath(__file__)),"./Ekran Resmi 2025-12-03 20.22.51.png"), cv2.IMREAD_COLOR)

# plt.imshow(img_bgr)

# print(img.shape)



img = cv2.imread(os.path.join(os.path.dirname(os.path.abspath(__file__)),"./Ekran Resmi 2025-12-03 20.22.51.png"))
cv2.imshow("Orijinal Resim", img)

cv2.waitKey()