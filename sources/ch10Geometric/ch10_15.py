# ch10_15.py
import cv2
import numpy as np

src = np.random.randint(0,256,size=[3,5],dtype=np.uint8)
rows, cols = src.shape
mapx = np.zeros(src.shape, np.float32)
mapy = np.zeros(src.shape, np.float32)
for r in range(rows):                               # 建立mapx和mapy
    for c in range(cols):
        mapx.itemset((r, c), cols-1-c)              # 設定mapx
        mapy.itemset((r, c), r)                     # 設定mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射
print(f"src =\n {src}")
print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")
print(f"dst =\n {dst}")


