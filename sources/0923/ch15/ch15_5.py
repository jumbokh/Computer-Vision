# ch15_5.py
import cv2

src = cv2.imread("easy.jpg")
src_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)     # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray,127,255,cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(dst_binary,
                      cv2.RETR_EXTERNAL,
                      cv2.CHAIN_APPROX_SIMPLE)
n = len(contours)                                   # 回傳輪廓數 
print(contours[1])                                  # 列印編號1的輪廓點







