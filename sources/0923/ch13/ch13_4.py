# ch13_4.py
import cv2

src = cv2.imread("map.jpg")
dst = cv2.Sobel(src, -1, 0, 1)      # 計算 y 軸影像梯度
cv2.imshow("Src", src)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

