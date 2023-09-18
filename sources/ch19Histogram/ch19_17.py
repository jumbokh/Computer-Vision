# ch19_17.py
import cv2

src = cv2.imread("springfield.jpg",cv2.IMREAD_COLOR)
cv2.imshow("Src", src)
(b, g, r) = cv2.split(src)              # 拆開彩色影像通道
blue = cv2.equalizeHist(b)              # 均衡化 B 通道
green = cv2.equalizeHist(g)             # 均衡化 G 通道
red = cv2.equalizeHist(r)               # 均衡化 R 通道
dst = cv2.merge((blue, green, red))     # 合併通道
cv2.imshow("Dst", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()



