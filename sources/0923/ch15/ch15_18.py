# ch15_18.py
import cv2

src = cv2.imread("easy.jpg")
cv2.imshow("src",src)                               # 顯示原始影像

src_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)     # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray,127,255,cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(dst_binary,
                      cv2.RETR_EXTERNAL,
                      cv2.CHAIN_APPROX_SIMPLE)  
n = len(contours)
for i in range(n):                                  # 繪製中心點迴圈
    M = cv2.moments(contours[i])                    # 影像矩
    area = cv2.arcLength(contours[i],True)          # 計算輪廓周長
    print(f"輪廓 {i} 周長 = {area}") 

cv2.waitKey(0)
cv2.destroyAllWindows()


