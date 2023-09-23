# ch15_10.py
import cv2
import numpy as np

src = cv2.imread("lake.jpg")
cv2.imshow("src",src)                               # 顯示原始影像

src_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)     # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray,150,255,cv2.THRESH_BINARY)
cv2.imshow("binary",dst_binary)                     # 顯示二值化影像
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(dst_binary,
                      cv2.RETR_LIST,
                      cv2.CHAIN_APPROX_SIMPLE)
mask = np.zeros(src.shape, np.uint8)
dst = cv2.drawContours(mask,contours,-1,(255,255,255),-1) # 繪製圖形輪廓
dst_result = cv2.bitwise_and(src,mask)
cv2.imshow("dst result",dst_result)                 # 顯示結果影像

cv2.waitKey(0)
cv2.destroyAllWindows()


