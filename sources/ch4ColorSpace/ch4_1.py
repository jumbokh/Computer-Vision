# ch4_1.py
import cv2

img = cv2.imread("view.jpg")                    # BGR 讀取
cv2.imshow("view.jpg", img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # BGR 轉 RBG
cv2.imshow("RGB Color Space", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()









 
