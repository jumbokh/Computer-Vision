# ch19_11.py
import cv2
import numpy as np

src = cv2.imread("macau.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
mask = np.zeros(src.shape[:2],np.uint8)             # 建立影像遮罩影像
mask[20:200,50:400] = 255                           # 在遮罩影像內建立遮罩
masked = cv2.bitwise_and(src, src, mask=mask)       # And運算
cv2.imshow("After Mask", masked)

cv2.waitKey(0)
cv2.destroyAllWindows()









