# ch13_12.py
import cv2

src = cv2.imread("lena.jpg",cv2.IMREAD_GRAYSCALE)
dst1 = cv2.Canny(src, 50, 100)      # minVal=50, maxVal=100
dst2 = cv2.Canny(src, 50, 200)      # minVal=50, maxVal=200
cv2.imshow("Src", src)
cv2.imshow("Dst1", dst1)
cv2.imshow("Dst2", dst2)

cv2.waitKey(0)
cv2.destroyAllWindows()

