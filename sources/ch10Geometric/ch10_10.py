# ch10_10.py
import cv2
import numpy as np

src = cv2.imread("tunnel.jpg")              # 讀取影像
cv2.imshow("Src",src)                       # 顯示原始影像

height, width = src.shape[0:2]              # 獲得影像大小
a1 = [0, 0]                                 # 原始影像的 A
b1 = [width, 0]                             # 原始影像的 B
c1 = [0, height]                            # 原始影像的 C
d1 = [width-1, height-1]                    # 原始影像的 D
srcp = np.float32([a1, b1, c1, d1])
a2 = [150, 0]                               # dst的 A
b2 = [width-150, 0]                         # dst的 B
c2 = [0, height-1]                          # dst的 C
d2 = [width-1, height-1]                    # dst的 D
dstp = np.float32([a2, b2, c2, d2])         
M = cv2.getPerspectiveTransform(srcp,dstp)  # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpPerspective(src, M, dsize)    # 執行透視
cv2.imshow("Dst",dst)                       # 顯示透視影像

cv2.waitKey(0)
cv2.destroyAllWindows()




