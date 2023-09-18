# ch10_1.py
import cv2

src = cv2.imread("southpole.jpg")       # 讀取影像
cv2.imshow("Src",src)                   # 顯示原始影像
width = 300                             # 新的影像寬度
height = 200                            # 新的影像高度
dsize = (width, height)
dst = cv2.resize(src, dsize)            # 重設影像大小
cv2.imshow("Dst",dst)                   # 顯示新的影像
    
cv2.waitKey(0)
cv2.destroyAllWindows()




