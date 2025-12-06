import cv2
import numpy as np

img = cv2.imread("./Ekran Resmi 2025-12-03 20.22.51.png")

while True:
    cv2.imshow("Image",img)
    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()


#Fare ile çizim yapma(left)

def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(param,(x,y),100,(255,0,0),1)

img = cv2.imread("./Ekran Resmi 2025-12-03 20.22.51.png")
cv2.namedWindow(winname="Image")
cv2.setMouseCallback("Image",draw_circle,img)

while True:
    cv2.imshow("Image",img)
    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()


#Fare ile çizim yapma(right)
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


import cv2
import numpy as np

drawing = False
ix,iy = -1,-1

def draw_rectangle(event,x,y,flags,param):
    global ix,iy,drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(param,(ix,iy),(x,y),(0,255,0),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(param,(ix,iy),(x,y),(0,255,0),-1)


img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow(winname="Image")
cv2.setMouseCallback("Image",draw_rectangle,img)

while True:
    cv2.imshow("Image",img)
    if cv2.waitKey(20) & 0xFF ==27:
        break

cv2.destroyAllWindows()