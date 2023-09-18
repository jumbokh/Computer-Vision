# ch4_4.py
import cv2

img = cv2.imread("jk.jpg")                          # BGR讀取
cv2.imshow("BGR Color Space", img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # BGR轉GRAY
cv2.imshow("GRAY Color Space", img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()









 
