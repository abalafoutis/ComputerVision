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

def score(x, y):
    if (img[x, y][0] == 255 and img[x, y][1] == 255 and img[x, y][2] == 255):
        return 10
    elif (img[x, y][0] == 0 and img[x, y][1] == 255 and img[x, y][2] == 0):
        return 20
    elif (img[x, y][0] == 255 and img[x, y][1] == 0 and img[x, y][2] == 0):
        return 40
    elif (img[x, y][0] == 255 and img[x, y][1] == 255 and img[x, y][2] == 0):
        return 60
    elif (img[x, y][0] == 0 and img[x, y][1] == 255 and img[x, y][2] == 255):
        return 100
    else:
        return 0

img = np.zeros((500,500,3),np.uint8)
drawTarget()

totalScore = 0

for i in range(3):
    x_random = random.randint(0, 500)
    y_random = random.randint(0, 500)
    redCross(x_random,y_random, 20)
    totalScore = totalScore + score(x_random, y_random)

cv2.putText(img, str(totalScore), (420,30), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,255), 2)
cv2.imshow("Image", img)
print(totalScore)

cv2.waitKey(0)
