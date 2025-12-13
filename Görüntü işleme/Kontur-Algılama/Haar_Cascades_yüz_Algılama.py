import numpy as np
import cv2
import matplotlib.pyplot as plt

nadia = cv2.imread("../Ders Notları/images/nadia.png")
denis = cv2.imread("../Ders Notları/images/denis.png")
solvay = cv2.imread("../Ders Notları/images/solvay_conference.jpg")

plt.imshow(nadia, cmap='gray')
plt.imshow(denis,cmap='gray')
plt.imshow(solvay,cmap='gray')


#Önceden eğitilmiş Haar Cascade Yüz Algılama Modelini Yükleme
#Fotodaki yüzleri algılamak için kullanacağız
face_cascade = cv2.CascadeClassifier("../Ders Notları/haar_cascades/haarcascade_frontalface_default.xml")


def detect_faces(img):
    
    face_img = img.copy()
    face_rects = face_cascade.detectMultiScale(face_img)

    for(x,y,w,h) in face_rects:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),10)

    return face_img

result = detect_faces(denis)
plt.imshow(result,cmap='gray')


result = detect_faces(nadia)
plt.imshow(result,cmap='gray')

result = detect_faces(solvay)
plt.imshow(result,cmap='gray')



def adj_detect_face(img):
    face_img = img.copy()

    face_rects = face_cascade.detectMultiScale(face_img,scaleFactor=1.2,minNeighbors=5)

    for(x,y,w,h) in face_rects:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),10)

    return face_img

result = adj_detect_face(solvay)
plt.imshow(result, cmap='gray')



eye_cascade = cv2.CascadeClassifier('../DATA/haarcascades/haarcascade_eye.xml')

def detect_eyes(img):
    face_img = img.copy()
    eyes = eye_cascade.detectMultiScale(face_img)

    for(x,y,w,h) in eyes:
        cv2.rectangle(face_img,(x,y),(x+w,y+h),(255,255,255),10)

    return face_img

result = detect_eyes(denis)
plt.imshow(result,cmap='gray')

eyes = eye_cascade.detectMultiScale(denis)
result = detect_eyes(denis)
plt.imshow(result,cmap='gray')



#Video ile bağlaç
cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()

    frame = detect_faces(frame)
    cv2.imshow('Video Face Detection', frame)

    c =cv2.waitKey(1)
    if c==27:
        break

cap.release()
cv2.destroyAllWindows()