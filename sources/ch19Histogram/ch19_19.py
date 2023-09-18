# ch19_19.py
import cv2
import matplotlib.pyplot as plt

src = cv2.imread("office.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src",src)
# 自適應直方圖均衡化
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
dst = clahe.apply(src)           # 灰度影像與clahe物件關聯
cv2.imshow("CLAHE",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


