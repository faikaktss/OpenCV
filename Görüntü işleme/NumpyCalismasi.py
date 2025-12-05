import numpy as np

array_list = [1,2,3,4,5]

np_array = np.array(array_list)#Diziyi numpy arrayine çevirme

np.arange(0,10)# 0'dan 10'a kadar olan sayıları içeren bir numpy arrayi oluşturma

np.arange(0,10,2)# 0'dan 10'a kadar olan sayılardan 2'şer artan bir numpy arrayi oluşturma

np.zeros((5,5))# 5x5 boyutunda tüm elemanları sıfır olan bir numpy arrayi oluşturma

np.ones((2,4))# 2x4 boyutunda tüm elemanları bir olan bir numpy arrayi oluşturma


np.random.seed(101)# Rastgele sayı üretiminde kullanılacak tohum değeri
arr = np.random.randint(0,100,10)# 0 ile 100 arasında 10 adet rastgele tam sayı içeren bir numpy arrayi oluşturma



mat = np.arange(0,100).reshape(10,10)# 0'dan 100'e kadar olan sayıları içeren ve 10x10 boyutunda yeniden şekillendirilmiş bir numpy arrayi oluşturma
row =0
col = 1

print(mat[row,col])# mat arrayinin 0. satır ve 1. sütunundaki elemanı yazdırma
print(arr.reshape(2,5))# Oluşturulan rastgele sayı arrayini 2 satır ve 5 sütun olacak şekilde yeniden şekillendirme
print("Random Array Mean:", arr.mean())
print("Random Array Max:", arr.max())
print(np.zeros((5,5)))
print(np.ones((2,4)))
print(np.arange(0,10,2))
print("Numpy Arange Array:", np.arange(0,10))
print("Numpy Array:", np_array)