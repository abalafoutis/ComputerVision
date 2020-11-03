import cv2
import numpy as np

img = cv2.imread("../images/lambo.png")

imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("Image", img)
cv2.imshow("Image HSV", imgHSV)
cv2.waitKey(0)