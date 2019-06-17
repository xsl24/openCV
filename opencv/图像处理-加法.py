import cv2
import numpy as np
a = cv2.imread("/Users/xushilun/Desktop/lenna.bmp",cv2.IMREAD_UNCHANGED)
b = a
#np加法和cv2加法的区别
add1 = a+b
add2 = cv2.add(a, b)

cv2.imshow("add1",add1)
cv2.imshow("add2",add2)
cv2.waitKey()
cv2.destroyAllWindows()