# ch10_6.py
import cv2
import numpy as np

src = cv2.imread("rural.jpg")                           # 讀取影像
cv2.imshow("Src",src)                                   # 顯示原始影像

height, width = src.shape[0:2]                          # 獲得影像大小
srcp = np.float32([[0,0],[width-1,0],[0,height-1]])     # src的A,B,C三個點
dstp = np.float32([[30,0],[width-1,0],[0,height-1]])    # dst的A,B,C三個點
M = cv2.getAffineTransform(srcp,dstp)                   # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(src, M, dsize)                     # 執行仿射
cv2.imshow("Dst",dst)                                   # 顯示傾斜影像

cv2.waitKey(0)
cv2.destroyAllWindows()




