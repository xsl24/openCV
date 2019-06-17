import cv2


a = cv2.imread("/Users/xushilun/Desktop/lenna.bmp")


b = cv2.resize(a,(200,100))


cv2.imshow("a",a)
cv2.imshow("b",b)

cv2.waitKey()
cv2.destroyAllWindows()