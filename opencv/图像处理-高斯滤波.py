import cv2

img = cv2.imread("/Users/xushilun/Desktop/lenna.bmp")
#0为上下翻转，>0左右翻转，<0上下左右都翻转
b = cv2.GaussianBlur(img,(13,13),0)


cv2.imshow("b",b)
cv2.waitKey()
cv2.destroyAllWindows()