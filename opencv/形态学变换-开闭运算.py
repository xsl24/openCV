import cv2
import numpy as np


img = cv2.imread("/Users/xushilun/Desktop/1396837-20190218131037437-2062323318.png")
k = np.ones((5,5),np.uint8)
#开运算
# dst = cv2.morphologyEx(img,cv2.MORPH_OPEN,k)
#闭运算
dst = cv2.morphologyEx(img,cv2.MORPH_CLOSE,k)
cv2.imshow("original",img)

cv2.imshow("dst",dst)


cv2.waitKey()
cv2.destroyAllWindows()