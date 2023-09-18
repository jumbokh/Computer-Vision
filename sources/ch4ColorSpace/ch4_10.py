# ch4_10.py
import cv2 
 
image = cv2.imread('street.jpg')
blue, green, red = cv2.split(image) 
bgr_image = cv2.merge([blue, green, red])   # 依據 B G R 順序合併
cv2.imshow("B -> G -> R ", bgr_image)

rgb_image = cv2.merge([red, green, blue])   # 依據 R G B 順序合併
cv2.imshow("R -> G -> B ", rgb_image)

cv2.waitKey(0)
cv2.destroyAllWindows()









 
