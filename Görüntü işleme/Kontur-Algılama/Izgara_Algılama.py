import cv2
import numpy as np
import matplotlib.pyplot as plt 

flat_chess = cv2.imread("../Ders Notları/images/flat_chessboard.png")
plt.imshow(flat_chess,cmap='gray')
plt.title("Düz Satranç Tahtası")
plt.show()


found , corners = cv2.findChessboardCorners(flat_chess,(7,7),None)
if found:
    print("Köşeler Bulundu")
else:
    print("Köşeler Bulunamadı")

print(corners.shape)

flat_chess_copy = flat_chess.copy()
cv2.drawChessboardCorners(flat_chess_copy,(7,7),corners,found)#Bulunan köşelerin üzerini çizer
plt.imshow(flat_chess_copy,cmap='gray')
plt.title("Köşelerin Üzerine Çizim")
plt.show()


#Çember Tabanlı Izgara Algılama
dots = cv2.imread("../Ders Notları/images/dot_grid.png")
plt.imshow(dots,cmap='gray')
plt.title("Nokta Izgarası")
plt.show()

found,corners = cv2.findCirclesGrid(dots,(4,11),None,cv2.CALIB_CB_SYMMETRIC_GRID)
print(found)

dbg_image_dircles = dots.copy()
cv2.drawChessboardCorners(dbg_image_dircles,(10,10),corners, found)
