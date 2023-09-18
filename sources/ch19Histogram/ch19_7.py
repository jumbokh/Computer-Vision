# ch19_7.py
import cv2

src = cv2.imread("snow.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Src", src)
hist = cv2.calcHist([src],[0],None,[256],[0,256])   # 直方圖統計資料
print(f"資料類型 = {type(hist)}")
print(f"資料外觀 = {hist.shape}")
print(f"資料大小 = {hist.size}")
print(f"資料內容 \n{hist}")



