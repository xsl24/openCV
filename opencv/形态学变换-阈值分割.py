import cv2
a = cv2.imread("/Users/xushilun/Desktop/lena512.bmp",cv2.IMREAD_UNCHANGED)

#二进制阈值化
# r,b = cv2.threshold(a,127,255,cv2.THRESH_BINARY)


#反二进制阈值化
# r,b = cv2.threshold(a,127,255,cv2.THRESH_BINARY_INV)

#截断阈值化
r, b = cv2.threshold(a, 127, 255, cv2.THRESH_TOZERO)



cv2.imshow("b",b)



cv2.waitKey()
cv2.destroyAllWindows()
