# ch19_12.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("macau.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
mask = np.zeros(src.shape[:2],np.uint8)                 # 建立影像遮罩影像
mask[20:200,50:400] = 255                               # 在遮罩影像內建立遮罩
hist = cv2.calcHist([src],[0],None,[256],[0,256])       # 灰階統計資料
hist_mask = cv2.calcHist([src],[0],mask,[256],[0,256])  # 遮罩統計資料
plt.plot(hist, color="blue", label="Src Image")         # 用plot()繪影像直方圖
plt.plot(hist_mask, color="red", label="Mask")          # 用plot()繪遮罩直方圖
plt.legend(loc="best")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()









