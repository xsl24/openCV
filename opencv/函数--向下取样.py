import cv2
o = cv2.imread("/Users/xushilun/Desktop/20140427204019875.png")

dst = cv2.pyrDown(o)


cv2.imshow("dst",dst)

cv2.waitKey()
cv2.destroyAllWindows()
"dddd"
