import cv2
import numpy as np

img = cv2.imread("../images/lena.png")

imgVer = np.vstack((img, img))

cv2.imshow("imgOutput", imgVer)
cv2.waitKey(0)
