# ch4_5.py
import cv2

pt_x = 169
pt_y = 118
img = cv2.imread("jk.jpg")              # BGR讀取
# BGR彩色轉成灰階GRAY
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY Color Space", img_gray)
px = img_gray[pt_x, pt_y]
print(f"Gray Color 通道值 = {px}")

# 灰階GRAY轉成BGR彩色
img_color = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
cv2.imshow("BGR Color Space", img_gray)
px = img_color[pt_x, pt_y]
print(f"BGR Color  通道值 = {px}")

cv2.waitKey(0)
cv2.destroyAllWindows()









 
