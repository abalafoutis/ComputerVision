import cv2
import numpy as np

img = np.zeros((500,500,3),np.uint8)

cv2.line(img, (0,0), (img.shape[1],img.shape[0]), (0,255,0), 3)

cv2.imshow("Green Diagonal", img)
cv2.waitKey(0)


