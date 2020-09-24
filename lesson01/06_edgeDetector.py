import cv2

img = cv2.imread("../images/lena.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgCanny = cv2.Canny(img,100,200)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Canny Image", imgCanny)
cv2.waitKey(0)


