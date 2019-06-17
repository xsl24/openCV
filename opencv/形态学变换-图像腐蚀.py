import cv2
import numpy as np


img = cv2.imread("/Users/xushilun/Desktop/test.png")
kernel = np.ones((5,5),np.uint8)
dst = cv2.erode(img,kernel=kernel,iterations=5)


cv2.imshow("original",img)

cv2.imshow("dst",dst)


cv2.waitKey()
cv2.destroyAllWindows()
