#drawing.py
import cv2
import numpy as np
img = cv2.imread('berry.jpg',cv2.IMREAD_COLOR)
# used to draw the line
cv2.line(img,(0,0),(150,150),(0,0,0),15)
#used for drawing the green rectangular 
cv2.rectangle(img,(15,25),(200,150),(0,255,0),2)
#
cv2.circle(img,(100,63),55,(0,0,255),6)
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#jjpts = pts.reshape(-1,1,2)
cv2.polylines(img,[pts],False,(0,255,255),3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'opencv tuts!',(0,130),font,1,(200,0,0),5,cv2.LINE_AA)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyALLWindows()
