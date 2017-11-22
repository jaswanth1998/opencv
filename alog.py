import cv2
import numpy as np

# Load two images
# 500 x 250
img1 = cv2.imread('ml1.png')
img2 = cv2.imread('mainlogo.png')

#add = img1+img2
rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]
img2gary = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask = cv2.threshold(img2gary,220,255,cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst
cv2.imshow('res',img1)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('img1_bg',img1_bg)
cv2.imshow('img2_fg',img2_fg)
#weighted = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
# cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

