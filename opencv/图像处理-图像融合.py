import cv2
import numpy as np
a = cv2.imread("/Users/xushilun/Desktop/lena.bmp",cv2.IMREAD_UNCHANGED)
b = cv2.imread("/Users/xushilun/Desktop/boat.bmp",cv2.IMREAD_UNCHANGED)
result = cv2.addWeighted(a,0.6,b,0.3,0)

cv2.imshow("result",result)
cv2.waitKey()
cv2.destroyAllWindows()