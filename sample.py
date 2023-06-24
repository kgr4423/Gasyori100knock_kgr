import cv2
import matplotlib as plt
import numpy as np

img = cv2.imread("assets/imori.jpg") #画像読込

print(img.shape) #画像のサイズ情報
print(img.dtype) #データの型

cv2.imshow("imori", img) #画像表示
cv2.waitKey(0) #キー入力があるまで待つ
cv2.destroyAllWindows() 

