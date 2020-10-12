import cv2
import numpy as np
import random

def drawTarget():
    cv2.circle(img, (250, 250), 250, (255, 255, 255), cv2.FILLED)
    cv2.circle(img, (250, 250), 200, (0, 255, 0), cv2.FILLED)
    cv2.circle(img, (250, 250), 150, (255, 0, 0), cv2.FILLED)
    cv2.circle(img, (250, 250), 100, (255, 255, 0), cv2.FILLED)
    cv2.circle(img, (250, 250), 50, (0, 255, 255), cv2.FILLED)

def redCross(x, y, size):
    cv2.line(img, (x-int(size/2), y), (x+int(size/2), y), (0, 0, 255), 3)
    cv2.line(img, (x, y-int(size/2)), (x, y+int(size/2)), (0, 0, 255), 3)

img = np.zeros((500,500,3),np.uint8)
drawTarget()
for i in range(3):
    x_random = random.randint(0, 500)
    y_random = random.randint(0, 500)
    redCross(x_random,y_random, 20)

cv2.imshow("Image", img)
cv2.waitKey(0)
