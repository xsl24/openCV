import cv2
import numpy as np
a = cv2.imread("/Users/xushilun/Desktop/2CC57A35A1C389B9283758D1C1B60BB9.jpg",cv2.IMREAD_UNCHANGED)
b =np.ones((101,101,3))
b= a[200:350,300:400]

a[0:50,0:100] =b
cv2.imshow("result",a)
cv2.imshow("face",b)
cv2.waitKey()
cv2.destroyAllWindows()