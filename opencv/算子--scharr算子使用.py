import cv2
import numpy as np
o = cv2.imread("/Users/xushilun/Desktop/lena.bmp")

scharrx = cv2.Scharr(o,cv2.CV_64F,1,0)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.Scharr(o,cv2.CV_64F,0,1)
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx,0.5,scharry,0.5,0)

cv2.imshow("xy",scharrxy)

cv2.waitKey()
cv2.destroyAllWindows()



