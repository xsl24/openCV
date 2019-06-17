import cv2
import numpy as np
a = cv2.imread("/Users/xushilun/Desktop/lenna.bmp",cv2.IMREAD_UNCHANGED)
b = cv2.cvtColor(a,cv2.COLOR_BGR2GRAY)
cv2.imshow("b",b)
cv2.imshow("a",a)
cv2.waitKey()
cv2.destroyAllWindows()