# ch4_3.py
import cv2

img = cv2.imread("view.jpg")                        # BGR讀取
cv2.imshow("view.jpg", img)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)      # BGR轉RBG
cv2.imshow("RGB Color Space", img_rgb)
img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)  # RGB轉BGR
cv2.imshow("BGR Color Space", img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()









 
