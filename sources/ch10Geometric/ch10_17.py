# ch10_17.py
import cv2
import numpy as np

src = cv2.imread("tunnel.jpg")
rows, cols = src.shape[:2]
mapx = np.zeros(src.shape[:2], np.float32)
mapy = np.zeros(src.shape[:2], np.float32)
for r in range(rows):                               # 建立mapx和mapy
    for c in range(cols):
        if 0.25*rows < r < 0.75*rows and 0.25*cols < c < 0.75*cols:
            mapx.itemset((r,c),2*(c - cols*0.25) )  # 計算對應的 x
            mapy.itemset((r,c),2*(r - rows*0.25) )  # 計算對應的 y
        else:
            mapx.itemset((r, c),0)                  # 取x座標為 0
            mapy.itemset((r, c),0)                  # 取y座標為 0   
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射

cv2.imshow("src",src)
cv2.imshow("dst",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()


