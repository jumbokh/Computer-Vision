# ch10_2.py
import cv2

src = cv2.imread("southpole.jpg")           # 讀取影像
cv2.imshow("Src",src)                       # 顯示原始影像
dst = cv2.resize(src,None,fx=0.5,fy=1.1)    # 重設影像大小
cv2.imshow("Dst",dst)                       # 顯示新的影像
print(f"src.shape = {src.shape}")
print(f"dst.shape = {dst.shape}")
    
cv2.waitKey(0)
cv2.destroyAllWindows()




