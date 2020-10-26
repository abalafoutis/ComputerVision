import cv2
import numpy as np

img = cv2.imread("../images/lena.png")

imgHor = np.hstack((img, img))
imgVer = np.vstack((imgHor, imgHor))

cv2.imshow("imgOutput", imgVer)
cv2.waitKey(0)
