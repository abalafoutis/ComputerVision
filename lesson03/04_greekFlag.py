import cv2
import numpy as np

img = np.zeros((180,400,3),np.uint8)
img[:] = 255,0,0

cv2.line(img, (100,30), (img.shape[1],30), (255,255,255), 15)
cv2.line(img, (0,50), (100,50), (255,255,255), 15)
cv2.line(img, (50,0), (50,110), (255,255,255), 15)
cv2.line(img, (100,70), (img.shape[1],70), (255,255,255), 15)
cv2.line(img, (0,110), (img.shape[1],110), (255,255,255), 15)
cv2.line(img, (0,150), (img.shape[1],150), (255,255,255), 15)

cv2.imshow("Greek Flag", img)
cv2.waitKey(0)