import cv2
import numpy as np

img = np.zeros((500,500,3),np.uint8)

cv2.line(img, (0,int(img.shape[1]/2)), (img.shape[0],int(img.shape[1]/2)), (0,0,255), 3)
cv2.line(img, (int(img.shape[0]/2), 0), (int(img.shape[0]/2), img.shape[1]), (0,0,255), 3)

cv2.imshow("Red Cross", img)
cv2.waitKey(0)

