# ch15_23.py
import cv2

# 讀取與建立影像 1
src1 = cv2.imread("mycloud1.jpg")
cv2.imshow("mycloud1",src1)
src1_gray = cv2.cvtColor(src1,cv2.COLOR_BGR2GRAY)       # 影像轉成灰階
# 二值化處理影像
ret, dst_binary = cv2.threshold(src1_gray,127,255,cv2.THRESH_BINARY)
# 找尋影像內的輪廓
contours, hierarchy = cv2.findContours(dst_binary,
                      cv2.RETR_LIST,
                      cv2.CHAIN_APPROX_SIMPLE)  
cnt1 = contours[0]
# 讀取與建立影像 2
src2 = cv2.imread("mycloud2.jpg")
cv2.imshow("mycloud2",src2)
src2_gray = cv2.cvtColor(src2,cv2.COLOR_BGR2GRAY)       # 影像轉成灰階
ret, dst_binary = cv2.threshold(src2_gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(dst_binary,
                      cv2.RETR_LIST,
                      cv2.CHAIN_APPROX_SIMPLE)  
cnt2 = contours[0]
# 讀取與建立影像 3
src3 = cv2.imread("explode1.jpg")
cv2.imshow("explode",src3)
src3_gray = cv2.cvtColor(src3,cv2.COLOR_BGR2GRAY)       # 影像轉成灰階
ret, dst_binary = cv2.threshold(src3_gray,127,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(dst_binary,
                      cv2.RETR_LIST,
                      cv2.CHAIN_APPROX_SIMPLE)  
cnt3 = contours[0]
sd = cv2.createShapeContextDistanceExtractor()          # 建立形狀場景運算子
match0 = sd.computeDistance(cnt1, cnt1)                 # 影像1和1比較 
print(f"影像1和1比較 = {match0}")
match1 = sd.computeDistance(cnt1, cnt2)                 # 影像1和2比較
print(f"影像1和2比較 = {match1}")
match2 =sd.computeDistance(cnt1, cnt3)                  # 影像1和3比較
print(f"影像1和3比較 = {match2}")
cv2.waitKey(0)
cv2.destroyAllWindows()


