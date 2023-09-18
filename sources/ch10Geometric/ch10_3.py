# ch10_3.py
import cv2

src = cv2.imread("python.jpg")                          # 讀取影像
cv2.imshow("Src",src)                                   # 顯示原始影像
dst1 = cv2.flip(src,0)                                  # 垂直翻轉
cv2.imshow("dst1 - Flip Vertically",dst1)               # 顯示垂直影像
dst2 = cv2.flip(src,1)                                  # 水平翻轉
cv2.imshow("dst2 - Flip Horizontally",dst2)             # 顯示水平影像
dst3 = cv2.flip(src,-1)                                 # 水平與垂直翻轉
cv2.imshow("dst3 - Horizontally and Vertically",dst3)   # 顯示水平與垂直影像
 
cv2.waitKey(0)
cv2.destroyAllWindows()




