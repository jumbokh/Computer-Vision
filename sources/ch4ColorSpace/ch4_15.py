# ch4_15.py
import cv2 
 
image = cv2.imread('street.jpg')
cv2.imshow("The Image", image)                  # 顯示BGR影像

bgra_image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
b, g, r, a = cv2.split(bgra_image)
print("列出轉成含A通道影像物件後的alpha值")
print(a)

a[:,:] = 32                                     # 修訂alpha內容
a32_image = cv2.merge([b, g, r, a])             # alpha=32影像物件
cv2.imshow("The a32 Image", a32_image)          # 顯示alpha=32影像

a.fill(128)                                     # 修訂alpha內容
a128_image = cv2.merge([b, g, r, a])            # alpha=128影像物件
cv2.imshow("The a128 Image", a128_image)        # 顯示alpha=128影像

cv2.waitKey(0)
cv2.destroyAllWindows()
      
cv2.imwrite('a32.png', a32_image)               # 儲存alpha=32影像
cv2.imwrite('a128.png', a128_image)             # 儲存alpha=128影像   







 
