# ch10_4.py
import cv2
import numpy as np

src = cv2.imread("rural.jpg")               # 讀取影像
cv2.imshow("Src",src)                       # 顯示原始影像

height, width = src.shape[0:2]              # 獲得影像大小
dsize = (width, height)                     # 建立未來影像大小
x = 50                                      # 平移 x = 50
y = 100                                     # 平移 y = 100
M = np.float32([[1, 0, x],
                [0, 1, y]])                 # 建立 M 矩陣                     
dst = cv2.warpAffine(src, M, dsize)         # 執行仿射
cv2.imshow("Dst",dst)                       # 顯示平移結果影像
 
cv2.waitKey(0)
cv2.destroyAllWindows()




