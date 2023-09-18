# ch19_13.py
import cv2
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread("macau.jpg",cv2.IMREAD_GRAYSCALE)
# 建立遮罩
mask = np.zeros(src.shape[:2],np.uint8)                 # 建立影像遮罩影像
mask[20:200,50:400] = 255                               # 在遮罩影像內建立遮罩
aftermask = cv2.bitwise_and(src,src,mask=mask)

hist = cv2.calcHist([src],[0],None,[256],[0,256])       # 灰階統計資料
hist_mask = cv2.calcHist([src],[0],mask,[256],[0,256])  # 遮罩統計資料
# subplot()第一個 2 是代表垂直有 2 張圖, 第二個 2 是代表左右有 2 張圖
# subplot()第三個參數是代表子圖編號
plt.subplot(221)                                        # 建立子圖 1
plt.imshow(src, 'gray')                                 # 灰階顯示第1張圖
plt.subplot(222)                                        # 建立子圖 2
plt.imshow(mask,'gray')                                 # 灰階顯示第2張圖
plt.subplot(223)                                        # 建立子圖 3
plt.imshow(aftermask, 'gray')                           # 灰階顯示第3張圖
plt.subplot(224)                                        # 建立子圖 4
plt.plot(hist, color="blue", label="Src Image")
plt.plot(hist_mask, color="red", label="Mask")
plt.legend(loc="best")
plt.show()











