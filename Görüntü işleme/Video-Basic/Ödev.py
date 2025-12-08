#Burada sadece bir görevin var. Bilgisayarınızdaki bir
#  kameradan canlı yayında okuyan bir program oluşturun
#  (veya kameranız yoksa, bir video
#  dosyası açmanız yeterlidir). Ardından,
#  sol fare düğmesini aşağı doğru her tıkladığınızda,
#  tıkladığınız yerin etrafında mavi bir daire
#  oluşturun. Son projenin nasıl görünmesi gerektiğine
#  dair bir örnek için videoya göz atın

import cv2
import numpy as np
import os



def draw_circle(event ,x,y,flags,param):

    global center ,clicked
    center = (0,0)
    clicked = False

    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x,y)
        clicked = False
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

cap  = cv2.VideoCapture(0)
cv2.namedWindow("Kamera")
cv2.setMouseCallback("Kamera",draw_circle)

while True:
    ret , frame = cap.read()
    if clicked == True:
        cv2.circle(frame,center,50,(255,0,0),2)
        cv2.imshow("Kamera",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

