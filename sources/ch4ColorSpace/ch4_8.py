# ch4_8.py
import cv2 
 
image = cv2.imread('mountain.jpg')
cv2.imshow('bgr', image)
blue, green, red = cv2.split(image) 
cv2.imshow('blue', blue)
cv2.imshow('green', green)
cv2.imshow('red', red)

print(f"BGR  影像 : {image.shape}")
print(f"B通道影像 : {blue.shape}")
print(f"G通道影像 : {green.shape}")
print(f"R通道影像 : {red.shape}")

cv2.waitKey(0)
cv2.destroyAllWindows()









 
