# ch13_7.py
import cv2

src = cv2.imread("lena.jpg")
dstx = cv2.Sobel(src, cv2.CV_32F, 1, 0)         # 計算 x 軸影像梯度
dsty = cv2.Sobel(src, cv2.CV_32F, 0, 1)         # 計算 y 軸影像梯度
dstx = cv2.convertScaleAbs(dstx)                # 將負值轉正值
dsty = cv2.convertScaleAbs(dsty)                # 將負值轉正值
dst =  cv2.addWeighted(dstx, 0.5,dsty, 0.5, 0)  # 影像融合
cv2.imshow("Src", src)
cv2.imshow("Dstx", dstx)
cv2.imshow("Dsty", dsty)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

