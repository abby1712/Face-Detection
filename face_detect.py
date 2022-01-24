import cv2
print(cv2.__version__)

face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_alt2.xml")

cam=cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

        

    cv2.imshow('Cam',frame)
    cv2.moveWindow('Cam',0,0)
    

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
