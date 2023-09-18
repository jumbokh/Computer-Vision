# ch10_5.py
import cv2

src = cv2.imread("rural.jpg")               # 讀取影像
cv2.imshow("Src",src)                       # 顯示原始影像

height, width = src.shape[0:2]              # 獲得影像大小
# 逆時鐘轉 30 度
M = cv2.getRotationMatrix2D((width/2,height/2), 30, 1)  # 建立 M 矩陣 
dsize = (width, height)                     # 建立未來影像大小                               
dst1 = cv2.warpAffine(src, M, dsize)        # 執行仿射
cv2.imshow("Dst - counterclockwise",dst1)   # 顯示逆時鐘影像

# 順時鐘轉 30 度
M = cv2.getRotationMatrix2D((width/2,height/2), -30, 1)  # 建立 M 矩陣                                
dst = cv2.warpAffine(src, M, dsize)         # 執行仿射
cv2.imshow("Dst clockwise",dst)             # 顯示順時鐘影像

cv2.waitKey(0)
cv2.destroyAllWindows()




