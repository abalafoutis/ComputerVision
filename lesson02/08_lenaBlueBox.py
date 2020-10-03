import cv2
import numpy as np

img = cv2.imread("../images/lena.png")
img[240:290, 240:360] = 255,0,0

cv2.imshow("Blue Box", img)
cv2.waitKey(0)


