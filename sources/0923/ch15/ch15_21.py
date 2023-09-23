#ch15_21.py
import cv2

src = cv2.imread("3shapes.jpg")
cv2.imshow("src", src)
src_gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)     # 影像轉成灰階

# 二值化處理影像
ret, dst_binary = cv2.threshold(src_gray,127,255,cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(dst_binary,
                      cv2.RETR_LIST,
                      cv2.CHAIN_APPROX_SIMPLE)

M0 = cv2.moments(contours[0])                       # 計算編號 0 影像矩 
M1 = cv2.moments(contours[1])                       # 計算編號 1 影像矩
M2 = cv2.moments(contours[2])                       # 計算編號 2 影像矩
Hu0 = cv2.HuMoments(M0)                             # 計算編號 0 Hu矩
Hu1 = cv2.HuMoments(M1)                             # 計算編號 1 Hu矩
Hu2 = cv2.HuMoments(M2)                             # 計算編號 2 Hu矩
# 列印Hu矩
print(f"h0 = {Hu0[0]}\t\t {Hu1[0]}\t\t {Hu2[0]}")
print(f"h1 = {Hu0[1]}\t\t {Hu1[1]}\t {Hu2[1]}")
print(f"h2 = {Hu0[2]}\t\t {Hu1[2]}\t {Hu2[2]}")
print(f"h3 = {Hu0[3]}\t\t {Hu1[3]}\t {Hu2[3]}")
print(f"h4 = {Hu0[4]}\t\t {Hu1[4]}\t {Hu2[4]}")
print(f"h5 = {Hu0[5]}\t\t {Hu1[5]}\t {Hu2[5]}")
print(f"h6 = {Hu0[6]}\t\t {Hu1[6]}\t {Hu2[6]}")

cv2.waitKey(0)
cv2.destroyAllWindows()


