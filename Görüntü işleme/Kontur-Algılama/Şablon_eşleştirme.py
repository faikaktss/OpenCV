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


# The full ımage to search

full = cv2.imread("../Ekran Resmi 2025-12-03 20.22.51.png")
fukk = cv2.cvtColor(full, cv2.COLOR_BGR2GRAY)


face = cv2.imread("../Ekran Resmi 2025-12-03 20.22.51.png")
face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for m in methods:
    ful_cop = full.copy()
    method = eval(m)
    res = cv2.matchTemplate(ful_cop,face,method)
    min_val, max_val, min_loc, max_loc = cv2.TM_SQDIFF_NORMED   

    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + face.shape[1], top_left[1] + face.shape[0])
    cv2.rectangle(ful_cop,top_left,bottom_right,255,10)
    
    plt.subplot(121)
    plt.imshow(res,cmap='gray')
    plt.title("Eşleştirme sonucu")

    plt.subplot(122)
    plt.imshow(ful_cop,cmap='gray')
    plt.title("Tespit Edilen Yer")

    plt.show()
    print('\n')
    print('\n')
