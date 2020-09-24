# Λεπτένοντας τις ακμές

import cv2
import numpy as np

img = cv2.imread("../images/lena.png")
kernel = np.ones((5,5), np.uint8)

imgCanny = cv2.Canny(img,150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgErode = cv2.erode(imgDialation, kernel, iterations=1)

cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Erode Image", imgErode)
cv2.waitKey(0)


