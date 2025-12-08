import cv2
import time

cap = cv2.VideoCapture("video.mp4") # Video dosyasını yükleme

fps = 25

if not cap.isOpened() == False:
    print("Error opening video file. Please double check your file path.")

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        time.sleep(1/fps)  # FPS hızına göre bekleme süresi
        cv2.imshow('Video', frame)  # Videoyu gösterme
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
    cap.release()

cv2.destroyAllWindows()