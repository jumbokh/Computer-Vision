# ch19_14.py
import cv2
import matplotlib.pyplot as plt

src = cv2.imread("snow1.jpg",cv2.IMREAD_GRAYSCALE)
plt.subplot(221)                        # 建立子圖 1
plt.imshow(src, 'gray')                 # 灰階顯示第1張圖
plt.subplot(222)                        # 建立子圖 2
plt.hist(src.ravel(),256)               # 降維再繪製直方圖
plt.subplot(223)                        # 建立子圖 3
dst = cv2.equalizeHist(src)             # 均衡化處理
plt.imshow(dst, 'gray')                 # 顯示執行均衡化的結果影像
plt.subplot(224)                        # 建立子圖 4
plt.hist(dst.ravel(),256)               # 降維再繪製直方圖
plt.show()


