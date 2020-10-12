import cv2
import numpy as np
import random

def redCross(x, y, size):
    cv2.line(img, (x-int(size/2), y), (x+int(size/2), y), (0, 0, 255), 3)
    cv2.line(img, (x, y-int(size/2)), (x, y+int(size/2)), (0, 0, 255), 3)

img = np.zeros((500,500,3),np.uint8)

for i in range(3):
    x_random = random.randint(0, 500)
    y_random = random.randint(0, 500)
    redCross(x_random,y_random, 20)

cv2.imshow("Red Cross", img)
cv2.waitKey(0)