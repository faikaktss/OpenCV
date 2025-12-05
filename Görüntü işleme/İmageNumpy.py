# import numpy as np
# import matplotlib.pyplot as plt
# from PIL import Image
# import os

# script_dir = os.path.dirname(os.path.abspath(__file__)) #Dosya yolunu alır
# pic = Image.open(os.path.join(script_dir, "Ekran Resmi 2025-12-03 20.22.51.png")) #Bu dosya yolunu kullanarak resmi açar

# pic_array = np.asarray(pic)
# print(pic_array.shape)

# plt.imshow(pic_array) # Sayısal diziyi matplotlib'e yükler 
# plt.show() # Burdada gösterir


# pic_red = pic_array.copy() 
# pic_red[:, :, 1] = 0
# pic_red[:, :, 2] = 0 

# plt.imshow(pic_red)

# print(type(pic))



#SORULAR
#1: Create a 5 by 5 array where every number is a 10

import numpy as np
import matplotlib.pylab as lpt
from PIL import Image
import os 

arr = np.ones((5,5))*10
print("5x5 Array with all elements as 10:\n", arr)


#2-: Rastgele sayılardan oluşan bir dizi oluşturmak için aşağıdaki hücreyi çalıştırın ve nasıl çalıştığını anlayıp anlayamayacağınızı görün.

np.random.seed(101)
arr = np.random.randint(low=0,high=100,size=(5,5))

print(arr.max())

#3-GÖREV: Okumak ve görüntülemek için PIL ve matplotlib kullanın .. /DATA/00-puppy.jpg görüntüsü.
script_dir = os.path.dirname(os.path.abspath(__file__))
pic = Image.open(os.path.join(script_dir,"./Ekran Resmi 2025-12-03 20.22.51.png"))
print(pic)

#4- Görüntüyü nump dizinine dönüştür
pic_arr = np.asarray(pic)
print(pic_arr.shape)