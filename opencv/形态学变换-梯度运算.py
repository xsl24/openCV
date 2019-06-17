import cv2
import numpy as np

img = cv2.imread("/Users/xushilun/Desktop/6B14532A-9FEC-4A90-BA90-6FA0F3277EC1.png")
k = np.ones((5,5,),np.uint8)
dst = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,k)

cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()