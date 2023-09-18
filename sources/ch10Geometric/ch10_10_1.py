# ch10_10_1.py
import cv2
import numpy as np

src = np.random.randint(0,256,size=[3,4],dtype=np.uint8)
rows, cols = src.shape
mapx = np.ones(src.shape, np.float32) * 3           # 設定 mapx
mapy = np.ones(src.shape, np.float32) * 2           # 設定 mapy
dst = cv2.remap(src, mapx, mapy, cv2.INTER_LINEAR)  # 執行映射
print(f"src =\n {src}")
print(f"mapx =\n {mapx}")
print(f"mapy =\n {mapy}")
print(f"dst =\n {dst}")


