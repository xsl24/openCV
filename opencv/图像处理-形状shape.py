import numpy
import cv2

img = cv2.imread("/Users/xushilun/Desktop/2CC57A35A1C389B9283758D1C1B60BB9.jpg",cv2.IMREAD_UNCHANGED)

#尺寸
print(img.shape)
#数据类型
print(img.dtype)
#像素点
print(img.size)