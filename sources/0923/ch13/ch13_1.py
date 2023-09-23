# ch13_1.py
import cv2
import numpy as np

src = np.random.randint(-256,256,size=[3,5],dtype=np.int16)
print(f"src = \n {src}")
dst = cv2.convertScaleAbs(src)
print(f"dst = \n {dst}")


