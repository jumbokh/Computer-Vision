# ch10_9.py
import cv2
import numpy as np

src = cv2.imread("rural.jpg")               # 讀取影像
cv2.imshow("Src",src)                       # 顯示原始影像

height, width = src.shape[0:2]              # 獲得影像大小
srcp = np.float32([[0,0],[width-1,0],[0,height-1]])
a = [0,height*0.4]                          # A
b = [width*0.8,height*0.2]                  # B
c = [width*0.1,height*0.9]                  # C
dstp = np.float32([a,b,c])                  # dst的 A, B, C
M = cv2.getAffineTransform(srcp,dstp)       # 建立 M 矩陣
dsize = (width, height)
dst = cv2.warpAffine(src, M, dsize)         # 執行仿射
cv2.imshow("Dst",dst)                       # 顯示傾斜影像

cv2.waitKey(0)
cv2.destroyAllWindows()




