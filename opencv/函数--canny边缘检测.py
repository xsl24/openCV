import cv2


o = cv2.imread("/Users/xushilun/Desktop/20140427204019875.png")

r = cv2.Canny(o,100,200)

cv2.imshow("r",r)


cv2.waitKey()
cv2.destroyAllWindows()