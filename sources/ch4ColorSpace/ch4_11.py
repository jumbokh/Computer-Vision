# ch4_11.py
import cv2 
 
image = cv2.imread('street.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

hue, saturation, value = cv2.split(hsv_image) 
hsv_image = cv2.merge([hue, saturation, value])   # 依據 H S V 順序合併

cv2.imshow("The Image", image)
cv2.imshow("The Merge Image", hsv_image)

cv2.waitKey(0)
cv2.destroyAllWindows()









 
