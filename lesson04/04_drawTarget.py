import cv2
import numpy as np

def drawTarget():
    cv2.circle(img, (250, 250), 250, (255, 255, 255), cv2.FILLED)
    cv2.circle(img, (250, 250), 200, (0, 255, 0), cv2.FILLED)
    cv2.circle(img, (250, 250), 150, (255, 0, 0), cv2.FILLED)
    cv2.circle(img, (250, 250), 100, (255, 255, 0), cv2.FILLED)
    cv2.circle(img, (250, 250), 50, (0, 255, 255), cv2.FILLED)

img = np.zeros((500,500,3),np.uint8)

drawTarget()

cv2.imshow("Image", img)
cv2.waitKey(0)
