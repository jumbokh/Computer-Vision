# ch19_18.py
import cv2

src = cv2.imread("office.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src",src)
equ = cv2.equalizeHist(src)             # 直方圖均衡化
cv2.imshow("euualizeHist",equ)

cv2.waitKey(0)
cv2.destroyAllWindows()


