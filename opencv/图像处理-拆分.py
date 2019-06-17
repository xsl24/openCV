import cv2

import  numpy as np

a = cv2.imread("/Users/xushilun/Desktop/lenna.bmp")
b,g,r = cv2.split(a)
cv2.imshow("original",a)
cv2.imshow("B",b)
cv2.imshow("G",g)
cv2.imshow("R",r)
#合并顺序不一样，图片也不一样
m = cv2.merge([b,g,r])
cv2.imshow("merg",m)
cv2.waitKey()


cv2.destroyAllWindows()