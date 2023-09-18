# ch10_16.py
import cv2
import numpy as np

src = cv2.imread("huang.jpg")
rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):                               # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), cols-1-c)              # 設定mapx
        mapy.itemset((r, c), r)                     # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

cv2.imshow("src",src)
cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


