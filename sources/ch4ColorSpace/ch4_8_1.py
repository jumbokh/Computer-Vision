# ch4_8_1.py
import cv2 
 
image = cv2.imread('mountain.jpg')
cv2.imshow('bgr', image)
blue, green, red = cv2.split(image) 
cv2.imshow('blue', blue)
cv2.imshow('green', green)
cv2.imshow('red', red)

print(f"BGR  影像 : {image.shape}")
print("B通道內容 : ")
print(blue)
print("G通道內容 : ")
print(green)
print("R通道內容 : ")
print(red)

cv2.waitKey(0)
cv2.destroyAllWindows()









 
