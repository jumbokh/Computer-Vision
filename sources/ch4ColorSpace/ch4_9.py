# ch4_9.py
import cv2 
 
image = cv2.imread('mountain.jpg')
cv2.imshow('bgr', image)

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hue, saturation, value = cv2.split(hsv_image) 
cv2.imshow('hsv', hue)
cv2.imshow('saturation', saturation)
cv2.imshow('value', value)
 
cv2.waitKey(0)
cv2.destroyAllWindows()









 
