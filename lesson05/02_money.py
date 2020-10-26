import cv2
import numpy as np

img = cv2.imread("../images/money.png")
imgResize = cv2.resize(img, (688, 447))

width,height = 370,200
points = np.float32([[101,262],[353,306],[78,396],[332,440]])
newPoints = np.float32([[0,0],[width,0],[0,height], [width,height]])

matrix = cv2.getPerspectiveTransform(points,newPoints)
imgOutput = cv2.warpPerspective(imgResize, matrix, (width,height))

cv2.imshow("Resized Image", imgResize)
cv2.imshow("imgOutput", imgOutput)
cv2.waitKey(0)
