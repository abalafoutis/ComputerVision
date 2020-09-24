import cv2

img = cv2.imread("../images/lena.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)  # το παράθυρο (7,7) πάντα μονός αριθμός!

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.waitKey(0)