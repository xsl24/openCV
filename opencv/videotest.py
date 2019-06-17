import cv2 as cv




capture = cv.VideoCapture("/Users/xushilun/Desktop/20190610_174607.mp4")
detector = cv.CascadeClassifier(cv.data.haarcascades +"haarcascade_frontalface_alt2.xml")

while True:
    ret,image =capture.read()
    if ret is True:

        faces = detector.detectMultiScale(image, scaleFactor=1.01,minNeighbors=1,minSize=(100,100),maxSize=(160,160))

        for x,y,width,height in faces:
            cv.rectangle(image,(x,y),(x+width,y+height),(0,0,255),2,cv.LINE_8,0)
        cv.imshow("faces",image)
        c = cv.waitKey(20)
        if c ==27:
            break
    else:
        break



cv.destroyAllWindows()
