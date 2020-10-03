import cv2
import numpy as np

img = np.zeros((512,512))  # Grayscale Image
print(img.shape)

cv2.imshow("Grayscale Black Image", img)
cv2.waitKey(0)