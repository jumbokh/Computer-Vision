# ch4_7.py
import cv2 
 
image = cv2.imread('colorbar.jpg')
cv2.imshow('bgr', image)
blue, green, red = cv2.split(image) 
cv2.imshow('blue', blue)
cv2.imshow('green', green)
cv2.imshow('red', red)

print(f"B通道影像屬性 shape = {blue.shape}")
print("列印B通道內容")
print(blue)
 
cv2.waitKey(0)
cv2.destroyAllWindows()









 
