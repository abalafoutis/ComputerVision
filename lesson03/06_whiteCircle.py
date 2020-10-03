import cv2
import numpy as np

img = np.zeros((500,500,3),np.uint8)

cv2.circle(img, (200,200), 100, (255,255,255), 3)

cv2.imshow("Image", img)
cv2.waitKey(0)


