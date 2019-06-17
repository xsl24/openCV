import cv2
import numpy as np

o = cv2.imread("/Users/xushilun/Desktop/lena.bmp")

sobelx = cv2.Sobel(o,cv2.CV_64F,1,0)
sobely = cv2.Sobel(o,cv2.CV_64F,0,1)
sobelx = cv2.convertScaleAbs(sobelx)
sobely = cv2.convertScaleAbs(sobely)
sobelxy = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)


cv2.imshow("xy",sobelxy)

cv2.waitKey()
cv2.destroyAllWindows()


