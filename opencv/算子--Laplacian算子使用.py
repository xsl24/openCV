import cv2
import numpy as np

o = cv2.imread("/Users/xushilun/Desktop/airfield.bmp")

laplacian = cv2.Laplacian(o,cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

cv2.imshow("laplacian",laplacian)


cv2.waitKey()
cv2.destroyAllWindows()