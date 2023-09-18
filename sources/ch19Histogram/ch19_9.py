# ch19_9.py
import cv2
import matplotlib.pyplot as plt

src = cv2.imread("macau.jpg",cv2.IMREAD_COLOR)
cv2.imshow("Src", src)
b = cv2.calcHist([src],[0],None,[256],[0,256])  # B 通道統計資料
g = cv2.calcHist([src],[1],None,[256],[0,256])  # G 通道統計資料
r = cv2.calcHist([src],[2],None,[256],[0,256])  # R 通道統計資料
plt.plot(b, color="blue", label="B channel")    # 用plot()繪 B 通道
plt.plot(g, color="green", label="G channel")   # 用plot()繪 G 通道
plt.plot(r, color="red", label="R channel")     # 用plot()繪 R 通道
plt.legend(loc="best")
plt.show()






