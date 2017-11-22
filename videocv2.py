import cv2
import numpy as np


#cv2.VideoCapture(0) it returns first webcam in the system 


cap = cv2.VideoCapture(1)
pac = cv2.VideoCapture(0)

#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',-1,20.0,(640,480))

while True:
	ret, frame = cap.read()
	ret, frame1 = pac.read()
	#frame = cv2.resize(frame, (640,480))
	#frame1 = cv2.resize(frame1, (640,480))


	
	#out.write(frame)
	cv2.imshow('frame',frame)
	#cv2.imshow('frame1',frame1)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
pac.release()
out.release()
cv2.destroyAllWindows()

#just checking 
