#imgOp.py
import cv2
import numpy as np

img = cv2.imread('berry.jpg',cv2.IMREAD_COLOR)

px = img[100,100]
print (px)
img[100,100] = [255,255,255]
px = img[100,100]
print(px)
#Region of image(roi)
roi = img[100:150,100:150]
print(roi)
img[100:150,100:150] = [255,255,255]
roi = img[100:150,100:150]


print(roi)

#coopying the img
berryImg = img[37:111,107:194]
img[0:74,0:87]=berryImg
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyALLWindows()

