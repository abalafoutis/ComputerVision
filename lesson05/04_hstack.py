import cv2
import numpy as np

img = cv2.imread("../images/lena.png")

imgHor = np.hstack((img, img))

cv2.imshow("Image Horizontal", imgHor)
cv2.waitKey(0)
