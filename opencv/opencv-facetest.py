import cv2 as cv



image = cv.imread("/Users/xushilun/Desktop/E9744567D11B2E6EC371F51F463F19DA.jpg")

h,w = image.shape[:2]

detector = cv.CascadeClassifier(cv.data.haarcascades +"haarcascade_frontalface_alt2.xml")

faces = detector.detectMultiScale(image, scaleFactor=1.06,minNeighbors=3,minSize=(30,30),maxSize=(w//3,h//3))

for x,y,width,height in faces:
    cv.rectangle(image,(x,y),(x+width,y+height),(0,0,255),2,cv.LINE_8,0)
cv.imshow("faces",image)
cv.waitKey(0)
cv.destroyAllWindows()
