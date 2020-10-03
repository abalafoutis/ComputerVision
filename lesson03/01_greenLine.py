import cv2
import numpy as np

img = np.zeros((500,500,3),np.uint8)

cv2.line(img, (100,250), (400,250), (0,255,0), 3)

cv2.imshow("Green Line", img)
cv2.waitKey(0)


