#OpenCV Bir USB Kameraya veya 
# Dizüstü Bilgisayar Kamerasına Bağlanma

import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#Görüntüyü gri tonlamaya çevirme
    cv2.imshow('Kamera',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()# Kamerayı serbest bırakma
cv2.destroyAllWindows()