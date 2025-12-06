import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


img = cv2.imread(os.path.join(os.path.dirname(os.path.abspath(__file__)),"./Ekran Resmi 2025-12-03 20.22.51.png"))
plt.imshow(img)


img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img_rgb)

#Dikdörtgen çizme
cv2.rectangle(img_rgb, pt1=(50,50), pt2=(200,200), color=(255,0,0), thickness=3)
plt.imshow(img_rgb)

#Görüntünün ortasına bir MAVİ ÜÇGEN çizin. Boyut ve açı size kalmış, ancak herhangi bir yönde bir üçgen (üç kenar) olmalıdır.
img_rgb = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
vertices = np.array([[250,100],[100,400],[400,400]], np.int32)
pts = vertices.reshape((-1,1,2))

cv2.polylines(img_rgb,[pts],isClosed=True,color=(0,0,255),thickness=20)
plt.imshow(cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB))

#Görüntünün içini boyamamız lazım
img_rgb = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
vertices = np.array([[250,100],[100,400],[400,400]], np.int32)
pts = vertices.reshape((-1,1,2))

cv2.fillPoly(img_rgb,[pts],color=(255,0,0)) #Bu üçgenin içini boyar
plt.imshow(cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB))





import numpy as np
import cv2

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(param,(x,y),100,(255,0,0),1)

img = cv2.imread("./Ekran Resmi 2025-12-03 20.22.51.png")
cv2.namedWindow(winname="Image")

cv2.setMouseCallback("Image",draw_circle,img)

while True:
    cv2.imshow("Image",img)
    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()