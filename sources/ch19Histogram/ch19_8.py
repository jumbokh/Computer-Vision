# ch19_8.py
import cv2
import matplotlib.pyplot as plt

src = cv2.imread("snow.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
hist = cv2.calcHist([src],[0],None,[256],[0,258])   # 直方圖統計資料
plt.plot(hist)                                      # 用plot()繪直方圖
plt.show()






