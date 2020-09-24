import cv2
import numpy as np

img = np.zeros((512,512))
print(img.shape)

cv2.imshow("Image", img)
cv2.waitKey(0)