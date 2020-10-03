import cv2
import numpy as np

img = np.zeros((500,500,3),np.uint8)
print(img.shape)
img[100:400, 100: 400] = 255,0,0

cv2.imshow("Black Image with Blue frame", img)
cv2.waitKey(0)

