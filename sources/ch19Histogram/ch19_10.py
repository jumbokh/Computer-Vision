# ch19_10.py
import cv2
import numpy as np

src = np.zeros([200,400],np.uint8)          # 建立影像
src[50:150,100:300] = 255                   # 在影像內建立遮罩
cv2.imshow("Src", src)

cv2.waitKey(0)
cv2.destroyAllWindows()









