# ch13_10.py
import cv2

src = cv2.imread("laplacian.jpg")
dst_tmp = cv2.Laplacian(src, cv2.CV_32F)    # Laplacian邊緣影像
dst = cv2.convertScaleAbs(dst_tmp)          # 轉換為正值
cv2.imshow("Src", src)
cv2.imshow("Dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

