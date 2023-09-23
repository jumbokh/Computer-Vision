# ch15_16.py
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
dst = cv2.drawContours(src,contours,-1,(0,255,0),5) # 繪製圖形輪廓

for c in contours:                                  # 繪製中心點迴圈
    M = cv2.moments(c)                              # 影像矩
    Cx = int(M["m10"] / M["m00"])                   # 質心 x 座標
    Cy = int(M["m01"] / M["m00"])                   # 質心 y 座標
    cv2.circle(dst,(Cx,Cy),5,(255,0,0),-1)          # 繪製中心點
cv2.imshow("result",dst)                            # 顯示結果影像

cv2.waitKey(0)
cv2.destroyAllWindows()


