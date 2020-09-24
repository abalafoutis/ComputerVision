import cv2

img = cv2.imread("../images/lena.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (27,27), 0)

imgGray[240:360, 240:360] = imgBlur[240:360, 240:360]

cv2.imshow("Blur Face", imgGray)
cv2.waitKey(0)