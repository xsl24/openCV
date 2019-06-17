import cv2
import numpy as np

i = cv2.imread("/Users/xushilun/Desktop/2CC57A35A1C389B9283758D1C1B60BB9.jpg",cv2.IMREAD_UNCHANGED)
print(i.item(10,39,0))
i.itemset((10,39,0),255)
print(i.item(10,39,0))
