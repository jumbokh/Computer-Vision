# ch19_6.py
import cv2
import matplotlib.pyplot as plt

src = cv2.imread("snow.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
plt.hist(src.ravel(),20)       # 降維再繪製直方圖
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

