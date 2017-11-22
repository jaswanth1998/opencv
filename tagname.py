import cv2
import numpy as np
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer()
recognizer.load('recog/trainner.yml')
faceCascade = cv2.CascadeClassifier("recog/haarcascade_frontalface_default.xml");
path = 'dataSet'


cam = cv2.VideoCapture(0)
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 5, 1, 0, 4)
while True:
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),1)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
	#if(conf<20):
    if(Id==1):
      Id="janu"
    elif(Id==3):
      Id="jk"
	  #elif(Id==3):
	   # Id="pooja"
          #else:
           #  Id="Unknown"'''

    cv2.cv.PutText(cv2.cv.fromarray(img),str(Id), (x,y+h),font, 255)
    cv2.imshow("tracing",img) 
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()

