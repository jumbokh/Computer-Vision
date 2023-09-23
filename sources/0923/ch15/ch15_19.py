# ch15_19.py
import cv2

src = cv2.imread("heart.jpg")
cv2.imshow("src",src)                               # 顯示原始影像

src_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)     # 影像轉成灰階
M = cv2.moments(src_gray)                           # 影像矩
nu20 = M['nu20']
print(f"歸一化中心矩 nu20 = {nu20}")
nu02 = M['nu02']
print(f"歸一化中心矩 nu02 = {nu02}")

Hu = cv2.HuMoments(M)                               # Hu矩
print(f"Hu \n {Hu}")                                # 列印Hu矩

result = Hu[0][0] - (nu20 + nu02)                   # 驗證Hu矩 0, h0
print(f"驗證結果 h0 - nu20 - nu02 = {result}")



